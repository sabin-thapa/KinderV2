from django.shortcuts import render, redirect, get_object_or_404
from second.models import Post, Images, Result, Foods, Attend
from second.models import Notice, Absentday, Presentday, SID, ROUTINES, Contacts

from second.models import Attachment, Tutorial, Course
from second.models import Grading
from second.models import Course
from second.models import Assignments, Submissions

from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.ult

from .forms import UserUpdateForm, ResultForm, ProfileUpdateForm, StudentRegisterForm, AttendanceForm, AbsentForm, ContactsForm

from .forms import UserUpdateForm, ResultForm, AssignmentForm, GradeForm, ProfileUpdateForm, StudentRegisterForm, AttendanceForm, AbsentForm, ContactsForm, SubmissionForm

from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from users.models import User_parents, User_teachers
from django import template

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.conf import settings

register = template.Library()


@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        receivers = User_parents.objects.filter(
            school=user.user_teachers.school, ChildGrade=user.user_teachers.grade)
        payload = {'head': data['head'], 'body': data['body']}
        for receiver in receivers:
            send_user_notification(
                user=receiver.user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})


@login_required
def teacherprofile(request):
    if(hasattr(request.user, 'user_teachers')):
        teachers = User_teachers.objects.filter(
            school=request.user.user_teachers.school)
    else:
        teachers = User_teachers.objects.filter(
            school=request.user.user_parents.school, grade=request.user.user_parents.ChildGrade)

    teacherlist = {
        'teachers': teachers
    }
    return render(request, 'teacherprofile.html', teacherlist)


@login_required
def parentprofiles(request):
    students = []
    students = SID.objects.filter(teacher=request.user)
    parents = []
    for student in students:
        print(student.childid)
        parents.append(User_parents.objects.filter(
            ChildID=student.childid).first())
        print(parents)
    parentlist = {
        'parents': parents
    }
    return render(request, 'parentprofiles.html', parentlist)


@login_required
def result(request):

    context = {
        'results': Result.objects.all()
    }
    return render(request, 'result.html', context)


def analytics(request):
    context = {}
    return render(request, 'second/analytics.html', context)


@login_required
def food(request):
    context = {
        'food': Foods.objects.all()
    }

    return render(request, 'food.html', context)


@login_required
def addresult(request):
    form = ResultForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('result')

    context = {
        'form': form,
    }
    return render(request, 'addresult.html', context)


@login_required
def registerchild(request):
    context = {

        'stid': SID.objects.all(),
    }
    return render(request, 'registerchild.html', context)


class RoutineListView(ListView):
    model = ROUTINES
    template_name = 'routine.html'
    context_object_name = 'routine'


class ResultDetail(DetailView):
    model = Result
    template_name = 'resultdetail.html'


def attendance(request):

    context = {

        'students': Attend.objects.all(),
    }
    return render(request, 'Attendance/attendance.html', context)


def present(request, id):
    student = Attend.objects.get(id=id)
    student1 = Presentday.objects.filter(
        name=student, date=datetime.date.today())
    if student1.exists():
        messages.error(request, 'Attendance already done for today!')

    else:
        student1 = Presentday.objects.create(
            name=student, date=datetime.date.today())

    return redirect('attendance')


def presentdecrease(request, id):
    student = Attend.objects.get(id=id)
    student1 = Presentday.objects.filter(
        name=student, date=datetime.date.today())
    student1.delete()
    return redirect('attendance')


def absent(request, id):
    student = Attend.objects.get(id=id)
    student1 = Absentday.objects.filter(
        name=student, date=datetime.date.today())
    if student1.exists():
        messages.error(request, 'Attendance already done for today!')
    else:
        student1 = Absentday.objects.create(
            name=student, date=datetime.date.today())

    return redirect('attendance')


def absentdecrease(request, id):
    student = Attend.objects.get(id=id)
    student1 = Absentday.objects.filter(
        name=student, date=datetime.date.today())
    student1.delete()
    return redirect('attendance')


class AttendanceDetailView(DetailView):
    model = Attend
    template_name = 'Attendance/attendance_detail.html'


@login_required
def postsandnotices(request):
    post_list = Post.objects.all()
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    context = {

        'posts': post_list,
        'notices': Notice.objects.all()[:6],
        'vapid_key': vapid_key,

    }

    return render(request, 'home.html', context)


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice_detail.html'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/home/home"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = "/home/home"

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['content', 'photo']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class SIDCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SID
    fields = ['full_name', 'roll', 'childid']
    template_name = 'addchild.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class ROUTINESCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ROUTINES
    fields = ['day', 'ten_ten45', 'ten45_eleven30', 'eleven45_twelve30',
              'twelve30_one15', 'two_two45', 'two45_three30']
    template_name = 'addroutine.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class ROUTINESDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ROUTINES
    success_url = "/home/routine"

    def test_func(self):
        routine = self.get_object()
        return True


class FoodsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Foods
    fields = ['day', 'food']
    template_name = 'add_food.html'
    success_url = '/../home/food'

    def form_valid(self, form):
        form.instance.teacher = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class NoticeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['title', 'content']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'photo']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    fields = ['title', 'content']
    template_name = 'notice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notice = self.get_object()
        if self.request.user == notice.author:
            return True
        return False


# def profile(request):
    # return render(request,'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


class RoutineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ROUTINES
    fields = ['day', 'ten_ten45', 'ten45_eleven30', 'eleven45_twelve30',
              'twelve30_one15', 'two_two45', 'two45_three30']
    template_name = 'addroutine.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        routine = self.get_object()
        return True


class ResultUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Result
    fields = ['name', 'subject1', 'subject2', 'subject3',
              'subject4']
    template_name = 'addresult.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        result = self.get_object()
        return True


def contacts(request):
    Contact_Form = ContactsForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            email = request.POST.get('email')
            message = request.POST.get('message')

            template = get_template('contacts_form.txt')
            context = {
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "Kinder",
                content,
                "Class Teacher" + '',
                [email],
                headers={'Reply To': email},

            )

            email.send()

            return render(request, 'suc.html')
    return render(request, 'sendemail.html', {'form': Contact_Form})


class CourseListView(ListView):
    model = Course
    template_name = "second/courses.html"
    context_object_name = 'course'


class CourseDetailView(DetailView):
    model = Course
    template_name = "second/course-detail.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     #Add in queryset
    #     context['tutorial'] = Tutorial.objects.all()
    #     return context


class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    fields = ['course_title']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['course_title', 'announcement', 'syllabus', 'course_plan']

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/home/courses/'

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class TutorialListView(ListView):
    model = Tutorial
    template_name = 'second/tutorials.html'
    context_object_name = 'tutorial'

    def get_queryset(self):
        return Tutorial.objects.all().order_by('-date_posted')


class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'second/tutorial_detail.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     #Add in queryset
    #     context['tutorial'] = Tutorial.objects.all()
    #     return context


class TutorialCreateView(LoginRequiredMixin, CreateView):
    model = Tutorial
    fields = ['course', 'title', 'video', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.course = self.request.course  HELP NEEDED
        return super().form_valid(form)


class TutorialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tutorial
    fields = ['course', 'title', 'video', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class TutorialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tutorial
    success_url = '/home/tutorials/'

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class AttachmentListView(ListView):
    model = Attachment
    template_name = 'second/attachments.html'
    context_object_name = 'attachment'

    def get_queryset(self):
        return Attachment.objects.all().order_by('-date_posted')


class AttachmentDetailView(DetailView):
    model = Attachment
    template_name = 'second/attachment_detail.html'


class AttachmentCreateView(LoginRequiredMixin, CreateView):
    model = Attachment
    fields = ['title', 'file', 'course']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def form_valid(self, form):
    #     course  = Course.objects.get(course_title = course_title)
    #     form.instance.subject = self.request.course
    #     return super().form_valid(form)


class AttachmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Attachment
    fields = ['title', 'file', 'course']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class AttachmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Attachment
    success_url = '/home/attachments/'

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


def assignments(request):

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('assignments')
    else:
        form = AssignmentForm()

    filtered_subs = Submissions.objects.filter(author=request.user)

    tasks = Assignments.objects.filter(author=request.user)
    all_tasks = Assignments.objects.all()
    context = {
        'fsubs': filtered_subs,
        'tasks': tasks,
        'all_tasks': all_tasks,
        'form': form,
    }
    return render(request, 'Assignments/assignments.html', context)


def submissions(request, assignment_id):
    assignment1 = get_object_or_404(Assignments, pk=assignment_id)

    if request.method == "POST":
        if 'add_submission' in request.POST:
            form = SubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.assignment = assignment1
                form.instance.date_submitted = datetime.date.today()
                form.save()

            return redirect('assignments')
    else:
        form = SubmissionForm()

    context = {
        'form': form,
        'assignment': assignment1,
        'subs': Submissions.objects.filter(assignment_id=assignment_id),
    }
    return render(request, 'Assignments/submissions.html', context)


def gradesubmissions(request, assignment_id, submission_id):
    submission1 = get_object_or_404(Submissions, pk=submission_id)

    if request.method == "POST":

        if 'add_grade' in request.POST:
            form = GradeForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.submission = submission1
                form.instance.assignment = submission1.assignment
                form.instance.date_graded = datetime.date.today()
                form.save()

            return redirect('submissions', assignment_id=assignment_id)
    else:
        form = GradeForm()

    context = {
        'form': form,
        'submission': submission1,
    }
    return render(request, 'Assignments/gradesubmissions.html', context)


def grade_update(request, assignment_id, grade_id):
    grade = get_object_or_404(Grading, pk=grade_id)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.save()
            return redirect('submissions', assignment_id=assignment_id)
    else:
        form = GradeForm(instance=grade)
    return render(request, 'Assignments/grade-update.html', {'form': form})


class AssignmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Assignments
    fields = ['title', 'description', 'file', 'deadline']
    template_name = 'Assignments/assignments_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False


class SubmissionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Submissions
    fields = ['file', 'description']
    template_name = 'Assignments/submission_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        return True


class AssignmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Assignments
    success_url = "/home/assignments"

    def test_func(self):
        assignment = self.get_object()
        return True


class SubmissionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Submissions
    success_url = "/home/assignments"

    def test_func(self):
        submission = self.get_object()
        return True

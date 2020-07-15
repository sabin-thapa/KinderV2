from django.shortcuts import render, redirect, get_object_or_404
from second.models import Post, StudentId, Attendance, Images, Food, Result, Foods,Attend
from second.models import Post, StudentId, Attendance, Images, Routine, Notice, Absentday, Presentday, SID, Events,ROUTINES, Contacts
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserUpdateForm, ResultForm, ProfileUpdateForm, StudentRegisterForm, AttendanceForm, RoutineForm, FoodForm, AbsentForm, ContactsForm
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from users.models import User_parents,User_teachers
@login_required
def routine(request):
    context = {
        'routine': Routine.objects.all()
    }

    return render(request, 'routine.html', context)

@login_required
def teacherprofile(request):
    if(hasattr(request.user,'user_teachers')):
        teachers=User_teachers.objects.filter(school=request.user.user_teachers.school)
    else:
        teachers=User_teachers.objects.filter(school=request.user.user_parents.school,grade=request.user.user_parents.ChildGrade)
    
    teacherlist={
        'teachers': teachers
    }
    return render(request, 'teacherprofile.html', teacherlist)

@login_required
def parentprofiles(request):
    students=[]
    students=SID.objects.filter(teacher=request.user)
    parents=[]
    for student in students:
        print(student.childid)
        parents.append(User_parents.objects.filter(ChildID=student.childid).first())
        print(parents)
    parentlist={
        'parents': parents
    }
    return render(request, 'parentprofiles.html', parentlist)

@login_required
def result(request):

    context = {
        'results': Result.objects.all()
    }
    return render(request, 'result.html', context)


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


class RoutineDetailView(DetailView):
    model = ROUTINES
    template_name = 'routine_detail.html'


class ResultDetail(DetailView):
    model = Result
    template_name = 'resultdetail.html'


def attendance(request):

    context = {
        'students': Attend.objects.all(),
    }
    return render(request, 'attendance.html', context)


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
    template_name = 'attendance_detail.html'


def postsandnotices(request):
    post_list = Post.objects.all()

    context = {
        'posts': post_list,
        'notices': Notice.objects.all().order_by('-date_posted'),
        'events' : Events.objects.all().order_by('-date_posted'),

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


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


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
    fields = ['title', 'content', 'photo']
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

class FoodsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Foods
    fields = ['day','food']
    template_name = 'add_food.html'
    success_url='/../home/food'
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


class EventsDetailView(DetailView):
    model = Events
    template_name = 'events_detail.html'

class EventsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    success_url = "/home/home"

    def test_func(self):
        events = self.get_object()
        if self.request.user == events.author:
            return True
        return False


class EventsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Events
    fields = ['title', 'content']
    template_name = 'events_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_teachers != '':
            return True
        return False

class EventsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'content']
    template_name = 'events_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        events = self.get_object()
        if self.request.user == events.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'photo']
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

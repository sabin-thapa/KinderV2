
from .views import PostDetailView, CourseDetailView, CourseListView, SIDCreateView, absentdecrease, presentdecrease, addresult, ResultDetail, ResultUpdate, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineDetailView, RoutineListView, RoutineUpdateView, NoticeCreateView, NoticeDeleteView, NoticeDetailView, NoticeUpdateView, AttendanceDetailView, present, absent
from .views import EventsCreateView, TutorialUpdateView, AttachmentListView, AttachmentCreateView, AttachmentUpdateView, AttachmentDetailView, AttachmentDeleteView
from .views import TutorialDeleteView, TutorialCreateView, TutorialDetailView, TutorialListView, CourseUpdateView, CourseDeleteView, EventsDetailView, CourseCreateView, EventsUpdateView, EventsDeleteView, ROUTINESCreateView, FoodsCreateView, contacts
from .views import PostDetailView, SIDCreateView, absentdecrease, presentdecrease, addresult, ResultDetail, ResultUpdate, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineDetailView, RoutineListView, RoutineUpdateView, NoticeCreateView, NoticeDeleteView, NoticeDetailView, NoticeUpdateView, AttendanceDetailView, present, absent
from .views import EventsCreateView, EventsDetailView, EventsUpdateView, EventsDeleteView, ROUTINESCreateView, FoodsCreateView, contacts, assignments, AssignmentDeleteView, submissions, gradesubmissions, SubmissionDeleteView, AssignmentUpdateView, SubmissionUpdateView

from . import views
from django.urls import path

from users import views as users_views
from django.urls import path
from . import views
from .views import EventsCreateView, EventsDetailView, EventsUpdateView, EventsDeleteView, ROUTINESCreateView, FoodsCreateView, contacts, assignments, AssignmentDeleteView, submissions, gradesubmissions
from .views import PostDetailView, SIDCreateView, absentdecrease, presentdecrease, addresult, ResultDetail, ResultUpdate, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineDetailView, RoutineListView, RoutineUpdateView, NoticeCreateView, NoticeDeleteView, NoticeDetailView, NoticeUpdateView, AttendanceDetailView, present, absent
from .views import EventsCreateView, EventsDetailView, EventsUpdateView, EventsDeleteView, ROUTINESCreateView, FoodsCreateView, contacts, grade_update
from .views import PostDetailView, CourseDetailView, CourseListView, SIDCreateView, absentdecrease, presentdecrease, addresult, ResultDetail, ResultUpdate, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineDetailView, RoutineListView, RoutineUpdateView, NoticeCreateView, NoticeDeleteView, NoticeDetailView, NoticeUpdateView, AttendanceDetailView, present, absent

urlpatterns = [
    path('home/', views.postsandnotices, name='home'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('notice/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'),
    path('notice/new/', NoticeCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/update', NoticeUpdateView.as_view(), name='notice-update'),
    path('notice/<int:pk>/delete', NoticeDeleteView.as_view(), name='notice-delete'),
    path('parent-profiles/', views.parentprofiles, name='parent-profiles'),
    path('teacher-profile/', views.teacherprofile, name='teacher-profile'),


    path('events/<int:pk>/', EventsDetailView.as_view(), name='events-detail'),
    path('events/new/', EventsCreateView.as_view(), name='events-create'),
    path('events/<int:pk>/update', EventsUpdateView.as_view(), name='events-update'),
    path('events/<int:pk>/delete', EventsDeleteView.as_view(), name='events-delete'),


    path('profile/', views.profile, name='profile'),
    path('registerchild/', views.registerchild, name='registerchild'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<int:pk>', AttendanceDetailView.as_view(),
         name='attendance-detail'),
    path('food/', views.food, name='food'),
    path('addfood/', FoodsCreateView.as_view(), name='add_food'),
    path('routine/', RoutineListView.as_view(), name='routine'),
    path('addroutine/', ROUTINESCreateView.as_view(), name='addroutine'),
    path('addchild/', SIDCreateView.as_view(), name='addchild'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('routine/<int:pk>/', RoutineDetailView.as_view(), name='routine-detail'),
    path('routine/<int:pk>/update',
         RoutineUpdateView.as_view(), name='routine-update'),
    path('result/', views.result, name='result'),
    path('addresult/', views.addresult, name='addresult'),
    path('presentdecrease/<id>/', views.presentdecrease, name="presentdecrease"),
    path('absent/<id>/', absent, name="absent"),
    path('present/<id>/', present, name="present"),
    path('absentdecrease/<id>/', views.absentdecrease, name="absentdecrease"),
    path('result/<int:pk>/update', ResultUpdate.as_view(), name='result-update'),
    path('result/<int:pk>/', ResultDetail.as_view(), name='result-detail'),
    path('contacts/', views.contacts, name='send-email'),

    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/new/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/',
         CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/',
         CourseDeleteView.as_view(), name='course-delete'),

    path('tutorials/', TutorialListView.as_view(), name='tutorials'),
    path('tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
    path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    path('tutorial/<int:pk>/update/',
         TutorialUpdateView.as_view(), name='tutorial-update'),
    path('tutorial/<int:pk>/delete/',
         TutorialDeleteView.as_view(), name='tutorial-delete'),

    path('attachments/', AttachmentListView.as_view(), name='attachments'),
    path('attachment/<int:pk>/', AttachmentDetailView.as_view(),
         name='attachment-detail'),
    path('attachment/new/', AttachmentCreateView.as_view(),
         name='attachment-create'),
    path('attachment/<int:pk>/update/',
         AttachmentUpdateView.as_view(), name='attachment-update'),
    path('attachment/<int:pk>/delete/',
         AttachmentDeleteView.as_view(), name='attachment-delete'),


    path('assignments/', views.assignments, name='assignments'),
    path('assignments/<int:pk>/update',
         AssignmentUpdateView.as_view(), name='assignment-update'),
    path('assignments/<int:pk>/delete',
         AssignmentDeleteView.as_view(), name='assignment-delete'),
    path('assignments/<int:assignment_id>/submissions', views.submissions,
         name='submissions'),
    path('submission/<int:pk>/update', SubmissionUpdateView.as_view(),
         name='submissions-update'),
    path('submission/<int:pk>/delete',
         SubmissionDeleteView.as_view(), name='submission-delete'),

    path('submissions/<int:submission_id>/', views.gradesubmissions,
         name='gradesubmissions'),
    path('grade/<int:submission_id>/update',
         views.grade_update, name='grade-update'),



]

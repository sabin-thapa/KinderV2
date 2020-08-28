from . import views
from django.urls import path
from users import views as users_views
from second import views as second_views

urlpatterns = [
    path('', views.index, name='index'),

    path('home.html', second_views.home, name='home'),
    path('dev.html', views.dev, name='dev'),
    path('queries.html', views.queries, name='queries'),
    path('services.html', views.services, name='services'),
    path('register_parent.html', users_views.register_parent, name="register_parent"),
    path('register_teacher.html', users_views.register_teacher, name="register_teacher"),
    path('signup.html', users_views.signup, name='signup'),
    path('contact.html', views.contact, name='contact'),


]

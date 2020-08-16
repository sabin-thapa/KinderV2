from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, User_p, User_t
from django.contrib.auth.models import User
from .models import User_parents,User_teachers
#from django.contrib.auth.decorators import login_required
from second import models as sm
from kinder.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        form1 = UserRegistrationForm(request.POST)
        form2 = UserRegistrationForm(request.POST)
        form_parents = User_p(request.POST)
        form_teachers = User_t(request.POST)
        students = sm.SID.objects.all()
        schools = sm.School.objects.all()
        parents = User_parents.objects.all()

        if form1.is_valid() and form_parents.is_valid():
            p = True
            for parent in parents:
                if form_parents.cleaned_data.get('ChildID') == parent.ChildID:
                    p = False
            access = False

            for student in students:
                if form_parents.cleaned_data.get('ChildID') == student.ChildID and p:
                    access = True
            if access:
                user = form1.save()
                profile = form_parents.save(commit=False)
                profile.user = user
                profile.save()

                username = form1.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect('login')

        if form2.is_valid() and form_teachers.is_valid():
            access=False
            for school in schools:
                
                if school.schcode == form_teachers.cleaned_data.get('schoolCode') and str(form_teachers.cleaned_data.get('school')) == school.sch:
                    access=True
            if access:
                user=form2.save()
                profile1= form_teachers.save(commit=False)
                profile1.user=user
                profile1.save()

                username = form2.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect('login')
    else:
        form1 = UserRegistrationForm()
        form_parents = User_p()
        form2 = UserRegistrationForm()
        form_teachers = User_t()

    return render(request, 'signup.html', {'form1': form1, 'form2': form2, 'form_parents':form_parents, 'form_teachers' : form_teachers})



def register_parent(request):
    if request.method == 'POST':
        form1 = UserRegistrationForm(request.POST)
        form_parents = User_p(request.POST)
        students=sm.SID.objects.all()
        parents=User_parents.objects.all()
            
        if form1.is_valid() and form_parents.is_valid():
            p=True
            for parent in parents:
                if form_parents.cleaned_data.get('ChildID') == parent.ChildID:
                    p=False
            access=False

            for student in students:
                if form_parents.cleaned_data.get('ChildID') == student.childid and p:
                    access=True
            if access:
                user=form1.save()
                profile= form_parents.save(commit=False)
                profile.user=user
                profile.save()

                username = form1.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect('login')
    else:
        form1 = UserRegistrationForm()
        form_parents = User_p()

    return render(request, 'register_parent.html', {'form1': form1, 'form_parents':form_parents})


def register_teacher(request):
    if request.method == 'POST':
        form2 = UserRegistrationForm(request.POST)
        form_teachers = User_t(request.POST)
        schools=sm.School.objects.all()

        if form2.is_valid() and form_teachers.is_valid():
            access=False
            for school in schools:
                
                if school.schcode == form_teachers.cleaned_data.get('schoolCode') and str(form_teachers.cleaned_data.get('school')) == school.sch:
                    access=True
            if access:
                user=form2.save()
                profile1= form_teachers.save(commit=False)
                profile1.user=user
                profile1.save()

                username = form2.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect('login')
    else:
        form2 = UserRegistrationForm()
        form_teachers = User_t()

    return render(request, 'register_teacher.html', {'form2': form2, 'form_teachers':form_teachers})

# Create your views here.
#@login_required
#def profile(request):
  #  return render(request,'profile.html')

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Kinder'
        message = 'Hope you are enjoying our website!! You can change your password by following the link: http://localhost:8000/password-reset-confirm/MjQ/set-password/'
        recepient = str(sub['Email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html',
            {'recepient': recepient})
    return render(request, 'reset.html', {'form':sub})
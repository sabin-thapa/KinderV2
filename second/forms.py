from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Result, StudentId, Attendance, Food, Foods, Contacts, Course
from .models import Profile, Result, StudentId, Attendance, Food, Foods, Contacts, Assignments, Submissions, Grading
from .models import Profile, StudentId, Attendance, Routine, Absentday
from bootstrap_datepicker_plus import DateTimePickerInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class StudentRegisterForm(forms.ModelForm):

    class Meta:

        model = StudentId

        fields = ('full_name', 'roll', 'childid')


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = ('full_name', 'roll', 'childid')


class ResultForm(forms.ModelForm):

    class Meta:

        model = Result

        fields = ('name', 'subject1', 'subject2', 'subject3',
                  'subject4', 'term')


class AbsentForm(forms.ModelForm):
    class Meta:
        model = Absentday
        fields = ['name', ]


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = {'email', 'message'}


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        widgets = {
            'deadline': DateTimePickerInput()
        }
        fields = ('title', 'description', 'file', 'deadline')


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ('file', 'description')


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grading
        fields = ('grade', 'remarks')

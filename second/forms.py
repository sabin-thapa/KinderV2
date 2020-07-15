from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Result, StudentId, Attendance, Food, Foods, Contacts
from .models import Profile, StudentId, Attendance, Routine, Absentday


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


class FoodForm(forms.ModelForm):

    class Meta:
        model = Foods
        fields = ('day', 'food')


class RoutineForm(forms.ModelForm):

    class Meta:

        model = Routine

        fields = ('day', 'ten_ten45', 'ten45_eleven30', 'eleven45_twelve30',
                  'twelve30_one15', 'two_two45', 'two45_three30')


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

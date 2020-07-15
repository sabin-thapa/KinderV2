from django.db import models
from django.contrib.auth.models import User
from second.models import School
# Create your models here.


class User_parents(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    UserType=models.CharField(max_length=20,default='parent')
    ChildID=models.IntegerField()
    ChildGrade=models.CharField(max_length=20)
    occupation = models.CharField(max_length=200)
    RelationToChild=models.CharField(max_length=200)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    

class User_teachers(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    UserType=models.CharField(max_length=20,default='teacher')
    age=models.IntegerField()
    grade=models.CharField(max_length=20)
    schoolCode=models.CharField(max_length=20)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    


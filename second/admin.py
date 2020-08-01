from django.contrib import admin
<<<<<<< HEAD
from second.models import Post, Profile, Result, StudentId, Attendance, Attend, Food, Routine, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES, Assignments, Submissions, Grading
=======
from second.models import Post, Tutorial, Profile, Result, StudentId, Attendance, Attend, Food, Course, Routine, Contacts, Absentday, Notice, Presentday, SID, School,Foods,ROUTINES

from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


>>>>>>> origin/resources

admin.site.register(StudentId)
admin.site.register(Attendance)
admin.site.register(Attend)
admin.site.register(Food)
admin.site.register(Foods)
admin.site.register(ROUTINES)
admin.site.register(Routine)
admin.site.register(Absentday)
admin.site.register(Presentday)
admin.site.register(SID)
admin.site.register(Result)
admin.site.register(School)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Notice)
admin.site.register(Contacts)
<<<<<<< HEAD
admin.site.register(Assignments)
admin.site.register(Submissions)
admin.site.register(Grading)
=======
admin.site.register(Course)
admin.site.register(Tutorial, MyModelAdmin)

>>>>>>> origin/resources
# Register your models here.

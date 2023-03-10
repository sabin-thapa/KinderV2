from second.models import Post,Room, Profile, Result, Attend, Course, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES
from second.models import Assignments, Submissions, Grading
from django.contrib import admin

from second.models import Post, Profile, Result, Attend, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES


from second.models import Tutorial, Attachment, Course
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Attend)
admin.site.register(Foods)
admin.site.register(ROUTINES)
admin.site.register(Absentday)
admin.site.register(Presentday)
admin.site.register(SID)
admin.site.register(Result)
admin.site.register(School)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Notice)
admin.site.register(Contacts)
admin.site.register(Course)
admin.site.register(Attachment)
admin.site.register(Tutorial, MyModelAdmin)
admin.site.register(Assignments)
admin.site.register(Submissions)
admin.site.register(Grading)
admin.site.register(Room)

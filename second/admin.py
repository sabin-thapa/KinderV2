from django.contrib import admin
from second.models import Post, Profile, Result, Attend, Contacts, Absentday, Notice, Presentday, SID, School, Foods, ROUTINES

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

# Register your models here.

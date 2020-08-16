from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField


class School(models.Model):
    sch = models.CharField(max_length=50)
    schcode = models.CharField(max_length=20, default='school')

    def __str__(self):
        return self.sch


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='posts', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date_posted"]


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)


class Events(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Events, self).save(*args, **kwargs)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + "Image"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StudentId(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()

    def __str__(self):
        return self.full_name


class SID(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('registerchild')

    def save(self, *args, **kwargs):
        super(SID, self).save(*args, **kwargs)
        Attend.objects.create(
            student=self)


class Attendance(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()

    def __str__(self):
        return self.full_name

    @property
    def absentdayss(self):
        return self.absentday_set.count()

    @property
    def presentdayss(self):
        return self.presentday_set.count()

    @property
    def days(self):
        return self.absentday_set.all()

    def get_absolute_url(self):
        return reverse('attendance-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Attendance, self).save(*args, **kwargs)


class Attend(models.Model):
    student = models.ForeignKey(SID, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.full_name

    @property
    def absentdayss(self):
        return self.absentday_set.count()

    @property
    def presentdayss(self):
        return self.presentday_set.count()

    @property
    def days(self):
        return self.absentday_set.all()

    def get_absolute_url(self):
        return reverse('attendance-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Attend, self).save(*args, **kwargs)


class Food(models.Model):
    day = models.CharField(max_length=30, null=True)
    food = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.day


class Foods(models.Model):
    day = models.CharField(max_length=30, null=True)
    food = models.CharField(max_length=30, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.day

    def save(self, *args, **kwargs):
        super(Foods, self).save(*args, **kwargs)


class Routine(models.Model):
    day = models.CharField(max_length=30)
    ten_ten45 = models.CharField(max_length=30)
    ten45_eleven30 = models.CharField(max_length=30)
    eleven45_twelve30 = models.CharField(max_length=30)
    twelve30_one15 = models.CharField(max_length=30)
    two_two45 = models.CharField(max_length=30)
    two45_three30 = models.CharField(max_length=30)

    def __str__(self):
        return self.day

    def get_absolute_url(self):
        return reverse('routine-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Routine, self).save(*args, **kwargs)


class ROUTINES(models.Model):
    day = models.CharField(max_length=30)
    ten_ten45 = models.CharField(max_length=30)
    ten45_eleven30 = models.CharField(max_length=30)
    eleven45_twelve30 = models.CharField(max_length=30)
    twelve30_one15 = models.CharField(max_length=30)
    two_two45 = models.CharField(max_length=30)
    two45_three30 = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.day

    def get_absolute_url(self):
        return reverse('routine-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(ROUTINES, self).save(*args, **kwargs)


class Absentday(models.Model):
    name = models.ForeignKey(Attend, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name.student.full_name + " A"


class Presentday(models.Model):
    name = models.ForeignKey(Attend, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name.student.full_name + " P"


class Result(models.Model):
    name = models.ForeignKey(SID, on_delete=models.CASCADE)
    subject1 = models.DecimalField(max_digits=4, decimal_places=1)
    subject2 = models.DecimalField(max_digits=4, decimal_places=1)
    subject3 = models.DecimalField(max_digits=4, decimal_places=1)
    subject4 = models.DecimalField(max_digits=4, decimal_places=1)
    term = models.CharField(max_length=30)

    def __str__(self):
        return self.name.full_name + "'s" + ' result '

    def get_absolute_url(self):
        return reverse('result-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Result, self).save(*args, **kwargs)


class Contacts(models.Model):
    email = models.EmailField()
    message = models.TextField()


class Course(models.Model):
    course_title = models.TextField()
    instructor   = models.ForeignKey(User, on_delete = models.CASCADE)
    announcement = models.TextField(null = True, blank=True)
    syllabus     = models.FileField(null= True, blank=True, upload_to='syllabus/', verbose_name="Syllabus")
    course_plan  = models.FileField(null = True, blank=True, upload_to = 'course_plan/', verbose_name = "Course Plan")


    def __str__(self):
        return self.course_title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)

    @property
    def syllabus_url(self):
        if self.syllabus and hasattr(self.syllabus, 'url'):
            return self.syllabus.url
        else:
            return None

    @property
    def course_plan_url(self):
        if self.course_plan and hasattr(self.course_plan, 'url'):
            return self.course_plan.url
        else:
            return None


class Tutorial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.TextField(null=True)
    video = EmbedVideoField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    desc = models.TextField(null=True)

    def __str__(self):
        return "%s - %s" % (self.author, self.title)

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('tutorial-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Tutorial, self).save(*args, **kwargs)


class Attachment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}\'s Attachment'

    class Meta:

        ordering = ['-date_posted']
    

    def get_absolute_url(self):
        return reverse('attachment-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Attachment, self).save(*args, **kwargs)


class Assignments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='assignments/',

                            null=True, blank=True,  verbose_name="File")

    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Assignments, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return (self.title + " by " + self.author.username)

    def get_absolute_url(self):
        return reverse('assignments')

    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
        else:
            return None


class Submissions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='submissions/',
                            null=True, blank=True, verbose_name="File")
    date_submitted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_submitted']

    def save(self, *args, **kwargs):
        super(Submissions, self).save(*args, **kwargs)

    def __str__(self):
        return ('Submission by ' + self.author.username)

    def get_absolute_url(self):
        return reverse('assignments')

    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
        else:
            return None


class Grading(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submissions, on_delete=models.CASCADE)
    grade = models.CharField(default="A", max_length=5)
    remarks = models.TextField(blank=True, null=True)
    date_graded = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        return super(Grading, self).save(*args, **kwargs)

    def __str__(self):
        return ('Grading for ' + self.submission.author.username + "'s submission for " + self.submission.assignment.title)

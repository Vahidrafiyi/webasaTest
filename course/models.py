from django.db import models
import datetime

from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save

class CourseCategory(models.Model):
    course_category = models.CharField(max_length=100)

    def __str__(self):
        return self.course_category

class Course(models.Model):

    class CourseLevel(models.TextChoices):
        BEGINNER = 'مبتدی'
        INTERMEDIATE = 'متوسط'
        PROFFESSIONAL = 'حرفه ای'

    class CourseStatus(models.TextChoices):
        PRE_REGISTRATION = 'پیش ثبت نام'
        RUNNING = 'در حال برگزاری'
        DONE = 'برگزار شده'

    course_title = models.CharField(max_length=120)
    course_category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE,default=1)
    course_related_category = models.ManyToManyField(CourseCategory,related_name='rel_cat')
    course_description = models.TextField()
    course_info = models.TextField(default='',null=True,blank=True)
    course_prerequisites = models.TextField(default='',null=True,blank=True)
    course_targets = models.TextField(default='',null=True,blank=True)
    course_audience = models.TextField(default='',null=True,blank=True)
    course_image = models.ImageField(upload_to='store_image/courses_image/',null=True, blank=True)

    course_price = models.IntegerField(default=1)
    course_discount_percent = models.IntegerField(default=0)
    course_discounted_price = models.IntegerField(default=1)

    course_syllabus = models.TextField(default='',null=True,blank=True)
    course_file = models.FileField(upload_to='files/course_files/',default='',blank=True,null=True)
    course_level = models.CharField(max_length=100, choices=CourseLevel.choices, default=CourseLevel.BEGINNER)
    course_status = models.CharField(max_length=100, choices=CourseStatus.choices, default=CourseStatus.RUNNING)
    course_duration = models.DurationField(default=datetime.timedelta(hours=40))
    course_start_date = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return self.course_title

@receiver(pre_save,sender=Course)
def calculate_course_discounted_price(sender,**kwargs):
    course = kwargs['instance']
    course.course_discounted_price = float(course.course_price)-(float(course.course_price)*float(course.course_discount_percent)/100)



# Generated by Django 3.2.7 on 2022-01-29 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=120)),
                ('course_description', models.TextField()),
                ('course_info', models.TextField(blank=True, default='', null=True)),
                ('course_prerequisites', models.TextField(blank=True, default='', null=True)),
                ('course_targets', models.TextField(blank=True, default='', null=True)),
                ('course_audience', models.TextField(blank=True, default='', null=True)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='store_image/courses_image/')),
                ('course_price', models.IntegerField(default=1)),
                ('course_discount_percent', models.IntegerField(default=0)),
                ('course_discounted_price', models.IntegerField(default=1)),
                ('course_syllabus', models.TextField(blank=True, default='', null=True)),
                ('course_file', models.FileField(blank=True, default='', null=True, upload_to='files/course_files/')),
                ('course_level', models.CharField(choices=[('مبتدی', 'Beginner'), ('متوسط', 'Intermediate'), ('حرفه ای', 'Proffessional')], default='مبتدی', max_length=100)),
                ('course_status', models.CharField(choices=[('پیش ثبت نام', 'Pre Registration'), ('در حال برگزاری', 'Running'), ('برگزار شده', 'Done')], default='در حال برگزاری', max_length=100)),
                ('course_duration', models.DurationField(default=datetime.timedelta(days=1, seconds=57600))),
                ('course_start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('course_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.coursecategory')),
                ('course_related_category', models.ManyToManyField(related_name='rel_cat', to='course.CourseCategory')),
            ],
        ),
    ]

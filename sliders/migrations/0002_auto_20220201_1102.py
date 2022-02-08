# Generated by Django 3.2.7 on 2022-02-01 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_button_text',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_link',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

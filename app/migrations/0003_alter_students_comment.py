# Generated by Django 4.0.4 on 2022-05-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_students_course_courses_number_of_students_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

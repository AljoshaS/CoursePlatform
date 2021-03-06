# Generated by Django 4.0.4 on 2022-06-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_instructors_instructor_of_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surename', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('skills', models.TextField()),
                ('education', models.TextField()),
                ('years_experience', models.IntegerField()),
                ('assistant_of_courses', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
        migrations.RenameModel(
            old_name='Instructors',
            new_name='Instructor',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]

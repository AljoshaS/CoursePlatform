# Generated by Django 4.0.4 on 2022-06-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_assistant_assistant_of_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='app.student'),
        ),
    ]

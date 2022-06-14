# Generated by Django 4.0.4 on 2022-05-29 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_courses_students_courses_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.courses'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-14 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_course_assistant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.assistant'),
        ),
    ]

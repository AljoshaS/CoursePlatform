# Generated by Django 4.0.4 on 2022-05-31 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='files',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.instructors'),
        ),
        migrations.AddField(
            model_name='files',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.students'),
        ),
    ]

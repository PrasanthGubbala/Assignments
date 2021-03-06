# Generated by Django 3.1.1 on 2020-11-15 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iLearn_App', '0007_delete_studentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('date', models.DateField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iLearn_App.scheduleclass')),
                ('id', models.ManyToManyField(to='iLearn_App.StudentRegistration')),
            ],
        ),
    ]

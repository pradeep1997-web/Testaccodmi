# Generated by Django 4.1.2 on 2022-12-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_student_subject_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]

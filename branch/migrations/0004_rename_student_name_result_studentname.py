# Generated by Django 4.1.2 on 2022-12-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='student_name',
            new_name='studentname',
        ),
    ]

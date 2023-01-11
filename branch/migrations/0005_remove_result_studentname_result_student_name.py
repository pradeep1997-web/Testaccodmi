# Generated by Django 4.1.2 on 2022-12-27 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_rename_student_name_result_studentname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='studentname',
        ),
        migrations.AddField(
            model_name='result',
            name='student_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='branch.student'),
        ),
    ]
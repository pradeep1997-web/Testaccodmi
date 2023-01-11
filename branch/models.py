from django.db import models

# Create your models here.
class Student(models.Model):
    SELECT_CLASS = (
        ("LKG", "LKG"),
        ("UKG", "UKG"),
        ("ONE", "One"),
        ("TWO", "Two"),
        ("THREE", "Three"),
        ("FOUR", "Four"),
        ("FIVE", "Five"),
        ("SIX", "Six"),
        ("SEVEN","Seven"),
        ("EIGHT","Eight"),
        ("NINE","Nine"),
        ("TEN","Ten"),
        ("ELAVON","Elavon"),
        ("TWELVE","Twelve"),
        ("BCA","BCA"),
        ("MCA","MCA"),
        ("BSC","Bsc"),
        ("BSC IT","Bsc IT"),
        ("BBA","BBA"),
        ("MBA","MBA"),
        ("MEDICAL","Medical"),
        ("OTHERS","Others")

    )
    SELECT_GENDER=(
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others"))

    student_name = models.CharField(max_length=40, null=True, blank=True)
    class_name=models.CharField(choices=SELECT_CLASS, max_length=255, default=False)
    subject_name = models.CharField(max_length=120, null=True, blank=True)
    roll_no =models.IntegerField(null=True)
    date_of_birthday = models.DateTimeField(auto_now=True)
    gender =models.CharField(choices=SELECT_GENDER, max_length=255, default=False,blank=True)
    mobile_no =models.IntegerField(null=True)

    def __str__(self):
        return str(self.student_name)


class Result(models.Model):
    student_name =models.ForeignKey(Student,null=True,on_delete=models.SET_NULL,blank=True)
    subject_name =models.CharField(max_length=40, null=True, blank=True)
    max_no =models.IntegerField(null=True)
    mark = models.IntegerField(null=True)
    remark =models.TextField(default="")

    def __str__(self):
        return str(self.id)

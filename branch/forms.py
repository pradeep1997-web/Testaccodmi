from django import forms
from .models import Student,Result
from django.core import validators

#DataFlair


class StudentRegistration(forms.ModelForm):
    SELECT_CLASS = (
        ("LKG", "LKG"),
        ("UKG", "UKG"),
        ("ONE", "One"),
        ("TWO", "Two"),
        ("THREE", "Three"),
        ("FOUR", "Four"),
        ("FIVE", "Five"),
        ("SIX", "Six"),
        ("SEVEN", "Seven"),
        ("EIGHT", "Eight"),
        ("NINE", "Nine"),
        ("TEN", "Ten"),
        ("ELAVON", "Elavon"),
        ("TWELVE", "Twelve"),
        ("BCA", "BCA"),
        ("MCA", "MCA"),
        ("BSC", "Bsc"),
        ("BSC IT", "Bsc IT"),
        ("BBA", "BBA"),
        ("MBA", "MBA"),
        ("MEDICAL", "Medical"),
        ("OTHERS", "Others")

    )
    SELECT_GENDER = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHERS", "Others"))

    student_name =forms.CharField()
    class_name=forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT_CLASS, label="Class")
    subject_name =forms.CharField()
    roll_no=forms.IntegerField(required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT_GENDER, label="Gender")
    date_of_birthday =forms.DateField(required = False)
    mobile_no = forms.IntegerField(required=False, min_value=0, )


    class Meta:
        model = Student
        fields = ['student_name','class_name','subject_name','roll_no','gender','mobile_no']



class StudentResultForm(forms.ModelForm):
    subject_name = forms.CharField()
    max_no=forms.IntegerField(required=False)
    mark =forms.IntegerField(required=False)
    remark= forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Remark"}))

    class Meta:
        model = Result
        fields = ['student_name','subject_name','max_no','mark','remark']

from django.shortcuts import render, redirect
from .models import Student,Result
from .forms import StudentRegistration,StudentResultForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    st_obj = Student.objects.all()
    return render(request, 'branch/home.html', {'st_obj': st_obj})


def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['student_name']
            cm = fm.cleaned_data['class_name']
            sm = fm.cleaned_data['subject_name']
            rn = fm.cleaned_data['roll_no']
            dby = fm.cleaned_data['date_of_birthday']
            gd = fm.cleaned_data['gender']
            ph = fm.cleaned_data['mobile_no']
            stud_obj = Student(student_name=nm, class_name=cm,subject_name=sm, roll_no=rn, date_of_birthday=dby, gender=gd, mobile_no=ph)
            stud_obj.save()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request,'branch/student_info_add.html',{"form":fm,"stu":stud})


def student_result(request):
    form= StudentResultForm()
    if request.method =='POST':
        form = StudentResultForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "your data saved ")
            return redirect('/')
    else:
        stud_result = Result.objects.all()
    return render(request,'branch/student_result.html',{"form":form,"stu":stud_result})


def java_sc_study(request):

    return render(request, 'branch/java_script.html')
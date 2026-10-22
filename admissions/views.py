from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
#from .forms import AdmissionForm
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm

def home(request):
    return render(request, 'home.html')
from .models import Admission, Course

def admission(request):

    courses = Course.objects.all()

    if request.method == "POST":

        student_name = request.POST.get("student_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        qualification = request.POST.get("qualification")
        course_id = request.POST.get("course")

        course = Course.objects.get(id=course_id)

        """Admission.objects.create(
            student_name=student_name,
            email=email,
            phone=phone,
            qualification=qualification,
            course=course
        )"""

        Admission.objects.update_or_create(
            user=request.user,
            defaults={
                'student_name': student_name,
                'email': email,
                'phone': phone,
                'qualification': qualification,
                'course': course,
            }
        )

        """Admission.objects.create(
            user=request.user,
            student_name=student_name,
            email=email,
            phone=phone,
            qualification=qualification,
            course=course
        )"""




























































        return render(request, "success.html")

    return render(request,
                  "admission_form.html",
                  {"courses": courses})
def courses(request):
    return render(request, 'courses.html')
"""def signup(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = StudentRegistrationForm()

    return render(request, 'signup.html', {'form': form})"""
def signup(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        else:
            print(form.errors)   # <-- Add this

    else:
        form = StudentRegistrationForm()

    return render(request, 'signup.html', {'form': form})
@login_required
def dashboard(request):
    admission = Admission.objects.filter(user=request.user).first()

    return render(
        request,
        "dashboard.html",
        {
            "admission": admission
        }
    )
    #return render(request, 'dashboard.html')

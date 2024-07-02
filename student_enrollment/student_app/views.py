from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, StudentForm
from .models import Student

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base2')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def base2(request):
    return render(request, 'base2.html')

def base(request):
    return render(request, 'base.html')

@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

@login_required
def view_students(request):
    if request.user.is_superuser:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(user=request.user)
    return render(request, 'view_students.html', {'students': students})

@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if not request.user.is_superuser and student.user != request.user:
        return redirect('view_students')

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if not request.user.is_superuser and student.user != request.user:
        return redirect('view_students')

    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'delete_student.html', {'student': student})


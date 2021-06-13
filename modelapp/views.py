from django.shortcuts import render, redirect
from modelapp.forms import AddStudentForm, UpdateStudentForm, UserRegistrationForm
from modelapp.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.

def index_page_view(request):
    return render(request, "modelapp/index.html")

################ Student add ###################################################
@login_required(login_url='/login/')
def add_student_view(request):
    form_obj = AddStudentForm()                        # create empty form default use GET method

    if request.method == "POST":              # if request.POST:
        form_obj = AddStudentForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print(form_obj)
            return redirect('/show/')

    return render(request, 'modelapp/add_student.html', {'form':form_obj})

################ Read Student ##################################################
@login_required(login_url='/login/')
def show_student_view(request):
    data = Student.objects.all()
    return render(request, "modelapp/show_student.html", {'data':data})

################## Update Student ##############################################
@login_required(login_url='/login/')
def update_student_view(request, id):
    obj = Student.objects.get(pk=id)
    form = UpdateStudentForm(instance=obj)

    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/show/')

    return render(request, "modelapp/update_student.html", {'form':form})

################ Delete Student ################################################
@login_required(login_url='/login/')
def delete_student_view(request, id):
    obj = Student.objects.get(pk=id)
    obj.delete()

    return redirect('/show/')

################# User Registration ############################################
def user_register_view(request):
    form = UserRegistrationForm()
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "modelapp/register.html", {'form':form})


######################## User login ############################################

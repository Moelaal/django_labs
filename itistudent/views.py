from django.shortcuts import render,redirect
# Create your views here.
from itistudent.models import students, Track,users
from  django.http import HttpResponseRedirect
from itistudent.forms import NewUserForm,StudentForm,studForm,studForm2
from django.views import View
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.views.generic import ListView,CreateView



def myhome(request):
    return render(request,'itistudent/home.html')


# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Registration successful." )
# 			# add myuser
# 			users.objects.create(name=request.POST['username'],password=request.POST['password1'])
# 			# # add user
# 			# User.objects.create_user(username=username,email=email,password1=password1,password2=password2)
# 			return redirect("itistudent:login")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="itistudent/register.html", context={"register_form":form})


# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			authuser = authenticate(username=username, password=password)
# 			# user = users.objects.filter(name=username,password=password)
# 			if (authuser is not None ):
# 				# request.session['username']=username
# 				login(request, authuser)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("itistudent:show")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="itistudent/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("itistudent:homepage")


class userCreateView(CreateView):
    model = users
    fields =  '__all__'

class trackCreateView(CreateView):
    model = Track
    fields =  '__all__'


class userList(ListView):
    model=users
    
class trackList(ListView):
    model=Track

def add(request):
	form = StudentForm(request.POST or None)
	# student = students.objects.all()
	if form.is_valid():
		form.save()
		# students.objects.create(name=request.POST['name'],age=request.POST['age'], track=request.POST['track'])
	return render(request,'itistudent/add.html',{'form': form})


def show(request):
	student = students.objects.all(
	)
	return render(request,'itistudent/show.html',{'student':student})

def update(request,id):
	student = students.objects.get(id=id)
	form = StudentForm(request.POST,instance=student)
	if form.is_valid():
		form.save()
		return redirect('itistudent:show')
	return render(request,'itistudent/update.html',{'student':student})

def delete(request, id):
	student = students.objects.get(id=id)
	if request.method == "POST":
		student.delete()
		return redirect('itistudent:show')

	context = {'student':student}
	return render(request, 'itistudent/delete.html', context)



def addusertoadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request,'itistudent/adduserAdmin.html',context)
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        users.objects.create(username=username,password=password)
        User.objects.create_user(username=username,email=email,password=password,is_staff="True")
        return render(request, 'itistudent/login.html', context)

def loginuserandadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request, 'itistudent/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        authuser = authenticate(username=username,password=password)
        user=users.objects.filter(username=username,password=password)

        if(authuser is not None and user is not  None):
            request.session['username']=username
            login(request, authuser)
            return redirect('/',user)
        else:
            context['msg'] = 'Invalid credentials'
            return render(request, 'itistudent/login.html', context)

def studentInserting(request):
    context = {}
    form = studForm()
    if (request.method == 'GET'):
        context['form'] = form
        return render(request, 'itistudent/insertstd.html', context)
    else:
        students.objects.create(name=request.POST['name'],age=request.POST['age'], track=request.POST['track'])
        return render(request, 'itistudent/home.html', context)


def insertStudentForm(request):
    context={}
    form=studForm2()
    if(request.method=='GET'):
        context['form']=form
        return render(request,'itistudent/insertstd.html',context)
    else:
        students.objects.create(name=request.POST['name'],age=request.POST['age'], track=request.POST['track'])
        return render(request, 'itistudent/home.html', context)
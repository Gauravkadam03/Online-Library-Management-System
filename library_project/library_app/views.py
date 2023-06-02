from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
# from .forms import createuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from datetime import date


# Home Page before login
def home(request):
    return render(request,'library_app/home.html')

# Home Page after login
@login_required(login_url='/signin/')
def index(request):
    return render(request,'library_app/index.html')

# Adding book data for Books table
@login_required(login_url='/signin/')
def form(request):
    if request.method=='POST':
        nm=request.POST.get('bname')
        an=request.POST.get('aname')
        dt=str(date.today())
        cat=request.POST.get('category')
        if book.objects.filter(B_name=nm).exists():
            return redirect('/display/')
        else:
            a=book(B_name=nm,A_name=an,Date=dt,B_category=cat)
            a.save()
        return redirect('/display/')
    return render(request,'library_app/form.html')

# Displaying book data 
@login_required(login_url='/signin/')
def display(request):
    data=book.objects.all()
    context={
        'data':data
    }
    if request.method=='POST':
        val=request.POST.get('val')
        data=book.objects.filter(B_name__contains=val)
        context1={
        'data':data
    }
        return render(request,'library_app/search_display.html',context1)
    return render(request,'library_app/display.html',context)

# Displaying book data with a link to update it 
@login_required(login_url='/signin/')
def display_update(request):
    data=book.objects.all()
    context={
        'data':data
    }
    return render(request,'library_app/display_update.html',context)

# By Book id updating the book data
@login_required(login_url='/signin/')
def update(request,j):
    data=book.objects.get(id=j)
    context={
        'data':data
    }
    if request.method=='POST':
        nm=request.POST.get('bname')
        an=request.POST.get('aname')
        dt=date.today()
        cat=request.POST.get('category')
        
        data.B_name=nm
        data.A_name=an
        data.Date=dt
        data.B_category=cat
        data.save()
        return redirect('/display/')

    return render(request,'library_app/update.html',context)

# Displaying book data with a link to Delete it 
@login_required(login_url='/signin/')    
def display_delete(request):
    data=book.objects.all()
    context={
        'data':data
    }
    return render(request,'library_app/display_delete.html',context)

# By Book id deleting the book data
@login_required(login_url='/signin/')
def delete(request,j):
    data=book.objects.get(id=j)
    context={
        'data':data
    }
    if request.method=='POST':
        data.delete()
        return redirect('/display/')
    return render(request,'library_app/delete.html',context)

# singnup view
def signup(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        # form=createuserform()
        # if request.method =='POST':
        #     form=createuserform(request.POST)
        #     if form.is_valid():
        #         form.save()
        #         user=form.cleaned_data.get('username')
        #         messages.success(request,'account was created for '+ user)
        #         return redirect ('/signin/')
          
          if request.method =='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            password1=request.POST.get('password1')
            if password!=password1:
                messages.error(request,'password not matched')
            else:
                if User.objects.filter(username=username).exists():
                    messages.error(request,'username taken')
                    return redirect ('/signup/')
                elif User.objects.filter(email=email).exists():
                    messages.error(request,'email taken')
                    return redirect ('/signup/')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return redirect ('/signin/')


    return render(request,'library_app/signup.html',{'form':form})


# signin view
def signin(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/index/')
            else:
                messages.info(request,'invalid credentials')
    return render(request,'library_app/a_login.html')

# logout view
@login_required(login_url='/signin/')
def logout(request):
    auth.logout(request)
    return redirect('/signin/')

# display students
@login_required(login_url='/signin/')
def display_students(request):
    data = User.objects.filter(is_staff=0)
    if request.method=='POST':
        val=request.POST.get('val')
        data=User.objects.filter(username__contains=val)
        context1={
        'data':data
    }
        return render(request,'library_app/search_student.html',context1)
    return render(request,'library_app/display_students.html',{'data':data})

# display student with delete button
@login_required(login_url='/signin/')
def delete_student(request):
    data = User.objects.filter(is_staff=0)
    return render(request,'library_app/delete_student.html',{'data':data})

# delete student by getting his id
@login_required(login_url='/signin/')
def delete_s(request,j):
    data=User.objects.get(id=j)
    context={
        'data':data
    }
    if request.method=='POST':
        data.delete()
        d = issue_book.objects.filter(s_id=j)
        d.delete()
        c = i_b_data.objects.filter(s_id=j)
        c.delete()
        return redirect('/display_stu/')
    return render(request,'library_app/del_std_d.html',context)

# issue book
@login_required(login_url='/signin/')
def issue_b(request,s_id,b_name,s_name):
    a = issue_book(s_id=s_id ,s_name=s_name, b_name=b_name)
    data = i_b_data.objects.filter(s_id=s_id)
    if len(data) == 0:
        data = issue_book.objects.filter(s_id=s_id)
        l =[]
        for i in data:
            l.append(i.b_name)
        if b_name in l:
            return redirect('/index/')
        else:
            a.save()
            return redirect('/index/')
    else:
        for i in data:
            if i.b_name == b_name:
                return redirect('/index/')
            else :
                data = issue_book.objects.filter(s_id=s_id)
                l =[]
                for i in data:
                    l.append(i.b_name)
                if b_name in l:
                    return redirect('/index/')
                else:
                    a.save()
                    return redirect('/index/')
    return render(request,'library_app/issue_b_disp.html',{'data':data})

# display issue book to specific student
@login_required(login_url='/signin/')
def display_iss_b(request,s_id):
    data = i_b_data.objects.filter(s_id=s_id)
    return render(request,'library_app/accept_data.html',{'data':data})

# admin and student navbar view issue books
@login_required(login_url='/signin/')
def dispaly_s_iss_b(request,v):
    if v == 0:
        data = issue_book.objects.all()
    else:
        data = issue_book.objects.filter(s_id=v)
    return render(request,'library_app/issue_b_disp.html',{'data':data})

# view issued book by admin
@login_required(login_url='/signin/')
def accpeted_data(request,s_id,b_name,s_name):
    a = i_b_data(s_id=s_id ,b_name=b_name, s_name=s_name, Date=date.today())
    a.save()  
    d = issue_book.objects.filter(s_id=s_id)            
    for i in d:
        if i.b_name == b_name:
            d = issue_book.objects.get(b_name=b_name)
            d.delete()
    data = i_b_data.objects.all()
    return render(request,'library_app/accept_data.html',{'data':data})

# admin view issued book to student
@login_required(login_url='/signin/')
def dis_accpeted_data(request):
    data = i_b_data.objects.all()
    return render(request,'library_app/accept_data.html',{'data':data})
    
# student return book view
@login_required(login_url='/signin/')
def del_accpeted_data(request,b_name,s_id):
    data = i_b_data.objects.filter(b_name=b_name)
    for i in data:
        if i.s_id == s_id:
            if b_name == i.b_name:
                d = i_b_data.objects.filter(id=i.id)
                d.delete()
    return redirect('/index/')



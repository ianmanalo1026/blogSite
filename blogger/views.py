from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import BlogPost
from .forms import CreateBlogForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signupuser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for[username]!')
            return redirect('home')   
    else:
        form = UserRegisterForm()
    return render(request, 'blogger/signupuser.html', {'form':form}) 
        
        
@login_required()
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'blogger/logoutuser.html')
        

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blogger/loginuser.html', {'form':AuthenticationForm()})
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
           return render(request, 'blogger/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match!'})
       else:
            login(request, user)
            return redirect('home')

def home(request):
    content = BlogPost.objects.all()
    return render(request, 'blogger/home.html', {'content':content})

def detail(request, blog_pk):
    content = get_object_or_404(BlogPost, pk=blog_pk)
    return render(request, 'blogger/detail.html', {'content':content})


    """
    User View
    """
@login_required()   
def mypage(request):
    content = BlogPost.objects.filter(blog_user=request.user)
    return render(request, 'blogger/mypage.html', {'content':content})    

@login_required()
def viewblog(request,blog_pk):
    content = get_object_or_404(BlogPost, pk=blog_pk, blog_user=request.user)
    return render(request, 'blogger/viewblog.html', {'content':content})

def myprofile(request):
    pass
    

@login_required()
def createblog(request):
    if request.method == 'GET':
        return render(request, 'blogger/createblog.html', {'form':CreateBlogForm()})
    else:
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            #the .blog_user in blog.blog_user should be the same name on the .models
            blog.blog_user = request.user
            blog.save()
            return redirect('mypage')
        
@login_required()          
def editblog(request, blog_pk):
    content = get_object_or_404(BlogPost, pk=blog_pk, blog_user=request.user)
    if request.method == 'GET':
        form = CreateBlogForm(instance=content)
        return render(request, 'blogger/editblog.html', {'content':content, 'form':form})
    else:
        try:
            form =  CreateBlogForm(request.POST, instance=content)
            form.save()
            return redirect('mypage')
        except ValueError:
            return render(request, 'blogger/editblog.html', {'content':content, 'form':form, 'error':'Please Try Again! '})
        
@login_required()       
def deleteblog(request, blog_pk):
    content = get_object_or_404(BlogPost, pk=blog_pk, blog_user=request.user)
    if request.method == "POST":
        content.delete()
        return redirect('mypage')
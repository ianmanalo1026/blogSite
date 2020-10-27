from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import BlogPost
from .forms import CreateBlogForm

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'blogger/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'blogger/signupuser.html', {'form':UserCreationForm(), 'error':'Username has been taken!'})
        else:
            return render(request, 'blogger/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match!'})
        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

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
    form = CreateBlogForm(instance=content)
    return render(request, 'blogger/detail.html', {'content':content, 'form':form})

def createblog(request):
    if request.method == 'GET':
        return render(request, 'blogger/createblog.html', {'form':CreateBlogForm()})
    else:
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blog_user = request.user
            blog.save()
            return redirect('home')
            
        
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from posts.models import Post
from index.models import SendMail

# Create your views here.
def home(request):
    posts = Post.objects.all()[0:3]
    context = {
        'posts': posts
    }
    if request.method == "POST":
        msgName = request.POST['name']
        msgEmail = request.POST['email']
        msg = request.POST['msg']
        mail = SendMail(name=msgName, email=msgEmail, msg=msg)
        mail.save()
        messages.success(request, 'Your message has been sent successfully.')
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'home.html', context)

def seemore(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'more.html', context)

def details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    if request.method == "POST":
        messages.success(request, 'Your booking has been accepted.')
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'details.html', context)

def search(request):
    query = request.GET['query']
    querytitle = Post.objects.filter(title__icontains=query)
    queryDesc = Post.objects.filter(desc__icontains=query)
    queryLocation = Post.objects.filter(location__icontains=query)
    queryCity = Post.objects.filter(city__icontains=query)
    queryState = Post.objects.filter(state__icontains=query)
    queryCategory = Post.objects.filter(category__icontains=query)
    queries = querytitle.union(queryDesc, queryLocation, queryCity, queryState, queryCategory)
    context = {
        'query': queries
    }
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'search.html', context)

def handle404(request, exception):
    return render(request, 'handle404.html')
from django.shortcuts import render, redirect
from .forms import ProfileForm, BlogPostForm, MyUserCreationForm
from django.contrib.auth.forms import UserCreationForm

def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            print(new_form)

            return redirect('/')
    if request.method == "GET":
        return render(request, "blogpost/create.html", {"form": BlogPostForm()})

def create_user(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/')
    if request.method == "GET":
        return render(request, "blogpost/user.html", {"form": MyUserCreationForm()}) 
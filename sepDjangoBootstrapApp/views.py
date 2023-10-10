from django.shortcuts import render

def home(request):
    return render(request, template_name="index.html")

def about(request):
    return render(request, template_name="about.html")

def gallery(request):
    return render(request, template_name="gallery.html")

def login(request):
    return render(request, template_name="login.html")

def Register(request):
    return render(request, template_name="Register.html")


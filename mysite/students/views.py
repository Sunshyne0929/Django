from django.shortcuts import render

def index(request):
    return render(request, 'students/index.html')

def profile(request):
    return render(request, 'students/profile.html')

def contact(request):
    return render(request, 'students/contact.html')

def home(request):
    return render(request, 'students/home.html')
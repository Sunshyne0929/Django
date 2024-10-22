from django.shortcuts import render

def index(request):
    return render(request, 'courses/index.html')

def detail(request):
    return render(request, 'courses/detail.html')

def instructors(request):
    return render(request, 'courses/instructors.html')

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')

def career(request):
    return render(request, 'main/career.html')
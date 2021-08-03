from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')

def accounts(request):
    return render(request, 'accounts.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def taxation(request):
    return render(request, 'taxation.html')


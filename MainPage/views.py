from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

def index(request):  
    return render(request, "MainPage.html")

def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('index') # or redirect('name-of-index-url')
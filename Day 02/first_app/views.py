# core django imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_function(request):
    return HttpResponse("Hello from django")

def home(request):
    return HttpResponse("home page")

def contact(request,**kwargs):
    status=kwargs.get('status')
    return HttpResponse(f"contact page {status}")
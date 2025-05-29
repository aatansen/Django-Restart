from django.shortcuts import render

# Create your views here.
def first_app(request):
    dynamic_data={
        'dt':'hello',
        'description':'Welcome to Django 5'
    }
    return render(request,'first_app/index.html',context=dynamic_data)
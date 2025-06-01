from django.shortcuts import render
from datetime import datetime

# Create your views here.
def first_app(request):
    date_time = datetime.now()

    dynamic_data={
        'dt':'hello',
        'description':'Welcome to Django 5',
        'date_time': date_time,
    }
    return render(request,'first_app/index.html',context=dynamic_data)
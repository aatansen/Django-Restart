from django.shortcuts import render
from datetime import datetime

# Create your views here.
def first_app(request):
    date_time = datetime.now()
    amount = [10.23647,10.000,10.36000]
    user_type = 'staff'
    dynamic_data={
        'dt':'hello',
        'description':'Welcome to Django 5',
        'date_time': date_time,
        'amount':amount,
        'user_type':user_type,
    }
    return render(request,'first_app/index.html',context=dynamic_data)
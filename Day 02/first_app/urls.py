# core django imports
from django.urls import path

# import from app
from first_app import views

urlpatterns = [
    path('',views.my_function,name='my_function'),
    path('home/',views.home,name='home'),
]
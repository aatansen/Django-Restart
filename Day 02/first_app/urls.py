# core django imports
from django.urls import path

# import from app
from first_app import views

urlpatterns = [
    path('',views.my_function,name='my_function'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,{'status':'ok'},name='contact'),
    path('contact-v2/',views.contact,{'status':'not ok'},name='contact'),
]
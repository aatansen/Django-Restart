# django core import
from django.urls import path

# custom app import
from first_app import views

urlpatterns = [
    path('',views.first_app,name='first_app'),
]

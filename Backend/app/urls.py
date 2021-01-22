from .views import *
from django.urls import path, include

urlpatterns = [
    path('register', register, name="register")
]

from .views import *
from django.urls import path, include

urlpatterns = [
    path('', register, name="register")
]

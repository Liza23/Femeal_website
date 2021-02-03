from .views import *
from django.urls import path, include

urlpatterns = [
    path('', register),
    path('blogs', blogs_view)
    # path()
]

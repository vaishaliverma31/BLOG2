from django.urls import path
from .views import *
urlpatterns = [
    path('blogapi',loginview.as_view())
]

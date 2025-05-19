from django.urls import path, include
from . import views
from .views import index


#define a list of urls patterns

urlpatterns = [
    path('', index, name="index"),

]
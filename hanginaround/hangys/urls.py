from django.urls import path, include
from . import views
from .views import index
from django.shortcuts import  render
from .form import ContactForm
from django.conf import settings
from django.conf.urls.static import static

#define a list of urls patterns

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('contact/', views.contact_view, name = 'contact'),
    path('contact/success', views.contact_success_view, name = 'contact-success'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
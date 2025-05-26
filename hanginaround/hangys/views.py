from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import ContactForm
from .models import Tour
# Create your views here.

def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}

    #return render(request, 'hangys/index.html', context)

def home_view(request):
    return render(request, 'tours/home.html')

#define contact_view to handle contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'tours/contact.html', context)

#Define the contact_success_view page
def contact_success_view(request):
    return render(request, 'tours/contact_success.html')
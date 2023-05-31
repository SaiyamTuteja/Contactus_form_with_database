from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from contactus.forms import ContactImage
from django.core.files.storage import FileSystemStorage


def contact(request):
    if request.method == 'POST':
        contact = Contact()

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.status = False

        form = ContactImage(request.POST, request.FILES)
        if form.is_valid():
            contact.save()
            img_obj = form.instance
            return HttpResponse("Your Data has been Saved")

    return render(request, 'index.html')


def demo(request):
    return render(request, 'home.html')

# Create your views here.

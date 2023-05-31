# Step 2:

Now open the project file with the `IDLE` you like to use

Open the terminal from your `IDLE` and type 
```commandline
python manage.py runserver
```

> And you are good to go. Open this link form you browser [http://localhost:8001/](http://localhost:8001/)
> 
> You will see the server is running
> 
> 

Now Let's Create an application which will run our ContactUS form

For Creating an Application type thi to your terminal

```commandline
python manage.py startapplications contactus
```

You can see now a new folder has ben created to your project directory

Now go to `settings.py` file you will find some list of installed application there

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
]
```

add the application name and save the file

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'contactus',
]
```

like this


After that go to the application folder and create a new file named `urls.py`. Now you just have to register the application url to the project url

Go back to project directory, you will find another `urls.py`, edit the file accordingly

```commandline
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contactus.urls')),
]
```

Now come back to Application directory and open `views.py` file

You can copy and paste the code from here

```commandline
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
```

After that go to `contactus/urls.py` file and add this line given billow

```commandline
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.contact, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

Now the server is ready to go

# Basic-Contact-Form-using-django-APPARKY

> In This Project we will create a functional ContactUs Page using [`Django FrameWork`](https://www.djangoproject.com/)
> 
> Let's get started with installing Django in your native system
> all the steps are followed in `steps` directory
> 

Before starting with this project active your Virtual Environment and run this command

```commandline
pthon-m pip install --upgrade pip

pip install -r requirement.txt
```

all necessary library will be installed and you are good to go.



## Step 1:

Create a Folder first and open it from CMD (Windows) or your native terminal

Install Django to your system by using this command

```commandline
pip install django
```

If done, create a new project file by typing this

```commandline
django-admin startproject YOURPROJECTNAME .
```

That's all. All your Native file will be created to yhe folder, and you are ready to start



## Step 2:

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



## Step 3:

Previously we are done creating the server. Here we will add some `HTML` file with it

You can find it from [Bootstrap](https://getbootstrap.com/)

> Now create a folder named `static` and `templates`
> 
> Again go to `settings.py` file and follow this step
> 
> Find `TEMPLATES` section and alter this with the given billow lines

```commandline
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
``` 

> You will also find `STATIC` section, alter it accordingly with the given lines

```commandline
STATIC_URL = '/static/'

MIDEA_URL = '/midea/'
MIDEA_ROOT = os.path.join(BASE_DIR, 'midea')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

```

In your project Directory, all `html` file will be stored in it, and other `css`, `js` and other fill will be at `static` folder.

You can create or Download it from [Bootstrap](https://getbootstrap.com/) and arrange them accordingly

Here `index.html` is containing the `ContactUs` Form.

In the next step we will discuss how to set up all `.css`, `.js` and other file with `.html` file



## Step 4:

Previously we discuss setting up the `application` and the `HTML`, here w will discuss the `jinga` technique to set up `.css`, `.js` and other files with `.html`


Replace all `.css`, `.js` and other file location like this command billow

```commandline
"{% static 'js/jquery.min.js' %}"
```

```commandline
"{% static '/css/style.css' %}"
```

Before replacing that make sure in the `static` folder you have created the necessary sub folder 

In this case `css` and `js` are the sub folders

-------------------















# Step 3:

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


















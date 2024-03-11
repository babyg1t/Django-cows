Cowsurf is a django application developed with the itensions of getting accustomed to this particular framework..

To replicate the app:

https://docs.djangoproject.com/en/5.0/intro/tutorial01/ 

~pip install django
~pip install virtualenv

Move to folder in which the project will be contained

virltualenv 'evnname'

django-admin startproject 'django_project'

source ./envname/bin/activate

Move to 'django_project'

python3 manage.py runserver

Console log:
---------------------------------------------
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 08, 2024 - 15:50:53
Django version 5.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
---------------------------------------------
python3 manage.py startapp 'myapp'

You should end up with something like that:
```
django_project/
    manage.py
    mysitename/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py		
```

add a:
```
    static/
	images/
```
folder

~python3 manage.py makemigrations 

~python3 manage.py migrate

```
django_projecct/
    myapp/
    manage.py
    db.sqite3
```

should be your end result 


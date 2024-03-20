Cowsurf is a django application developed with the itensions of getting accustomed to this particular framework..

To replicate the app:

https://docs.djangoproject.com/en/5.0/intro/tutorial01/ 

STEP 1:

Move to folder in which the project will be contained
~pip install virtualenv

~virtualenv env

source ./env/bin/activate
```
~pip install django
~pip install Pillow
~python -m pip install django_tables2
~pip install djangorestframework
```
STEP 2:

git clone https://github.com/babyg1t/Django-cows



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


You should end up with something like that:
```
myFolder/
    django_project/
        manage.py
        base/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
        myapp/
            migrations/
                __init__.py

            templates/
                __init__.py
            apps.py        
            models.py
            tests.py
            views.py
            admin.py
            forms.py
            urls.py
            tables.py
			
```
STEP 3:

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
    static/
	images/
```
should be your end result 

Another way without cloning this repository is to 
start your own django project with :

~django-admin startproject 'foo'

~cd /foo

~python3 manage.py startapp 'foobar'

Then copy and paste the repositorys' 
/base
/myapp
/migrations
/templates

Then proceed normally to STEP 3
You should be good to go!





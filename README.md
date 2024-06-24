Django Tutorial: https://youtu.be/t-uAgI-AUxc?si=91T22G6-WNW1SNxd

Step 1) Start a new django project named "mysite"
```shell
django-admin startproject mysite
```

Step 2) Create a new app named "api"

Run the command below in "mysite" directory
```shell
python manage,py startapp api
```

Step 3) Connect api with the main my site project
- Add the application in mysite/settings.py

Step 4) Create model for ORM
- Add a model in mysite/api/models.py

Step 5) Converts Model to JSON
- Add a new Model Serializer in mysite/api/serializers.py

Step 6) Create view that use the Model and the Serializer
- mysite/api/views.py
- Generic view that create a new blog post and get all the blog post that exist

Step 7) Define URL
- Create a route to "api" app in mysite/mysite/urls.py
- Create a route to the view in mysite/api/urls.py

Step 8) Database Migration 
- Use Django ORM to create the SQL tables

Run the command below in "mysite" directory
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```

Step 9) To run the server
```shell
python manage.py runserver
```

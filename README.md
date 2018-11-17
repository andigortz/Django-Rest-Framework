<p align="center"><img src="https://www.django-rest-framework.org/img/logo.png" alt="Django Rest Framework"></p>


                                                                                                                                      
# Django Rest Framework

-RestfulAPI is simple implementation of Django Rest Framework (DRF) with only User & Todos (you can't have override method likes Update, Delete, Put or Create)

-Djangorest is one example of a form of test driven approach with features such as CRUD and customizable administrator (you must create a superuser first if you wanna to try admin dashboard)

-Serialization focusing to create a simple API web and give comprehensive features to understanding Django Rest Framework on based serializers views (command execute in browser use `http://127.0.0.1:8000/todos`)

-Request and Response is one of the main core of Django Rest Framework. Request objects similar to the regular `HttpResponse` but more flexible and works well with web API, meanwhile Response uses to determine the correct/wrong content that return to client (command execute in browser use `http://127.0.0.1:8000/todos`)

# Bug
-Minor bug in djangorest 

# Requirements
1. Python version 3.5 or higher
2. Django version 2.x.x or higher `pip install django` on Windows
3. Django Rest Framework `pip install djangorestframework` 
4. Django coreapi (optional)
5. Pygments (optional) if you want to highlighting the code
6. Httpie or Curl (optional)

# How to use?
1. Download or clone this repository
2. Instal the requirements
3. Make sure create virtual environment
4. Migrate the database `python manage.py makemigrations` the `python manage.py migrate`
5. Start server `python manage.py runserver`
6. Open up in browser or using httpie
7. Finish and feel free to explore the codes

# Contribute
-if you want to contribute or discover a bug just send a pull request :)

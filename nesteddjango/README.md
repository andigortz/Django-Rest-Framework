# Nested API with Django Rest Framework

Simple implementation about nested routers in django rest framework. Nested built in django will allows us to create subrouters to register nested endpoints. It’s almost as simple as registering normal routers

# Prerequisite

1. Django Rest Framework `pip install djangorestframework`
2. Django Extensions `pip install drf-extensions`
3. Django Framework `pip install django`
4. Virtual environment

# How to Use

1. Download this repository
2. Make a migrations first `py manage.py migrate`
3. Runserver using `py manage.py runserver`
4. Navigate to `http://127.0.0.1:8000/api/authors/1/books/1/editions/` for see the instance endpoints
5. You can add the data in `http://127.0.0.1:8000/api/authors/`
6. If you found any error please contact me

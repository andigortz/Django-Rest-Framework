# Django Rest Framework

This is my complete project / tutorial and documentation about Django Rest Framework. And i think it's beginner friendly guide if you want to dive 
and more exploring about Django Rest Framework. Basically, this project contain **Serialization**, **Request and Responses**, **Authentication & Permissions**,
**Hyperlinked Relationship** and **Schema Libraries**. I skipped in class based views because it's already in my another project and also **Viewsets and Router**.
I think, for routers and viewset are used if for making APIs on a large scale or if we want to handle a URL automatically then we will use that method. However, 
for this tutorial because we manually route it, I don't think we need to use that method. 

This project allow us to post a data in django administrator then we can see it as a User and Admin in browsable API. That's kinda a repetitive if we want to post
a data so i'm adding a permissions to our API that only authenticated User can access in browsable API. Authenticate user are able to create, update, delete code
snippet in web API **not** in django administrator, meanwhile admin can't delete or edit a data that already create by user. This option only applies in browsable API.


**Main References** 
1. https://www.django-rest-framework.org/  
2. https://www.djangoproject.com/

**Project Setup**
1. If you are new to django, make sure create a virtual environment first `pip install virtualenvwrapper-win` then `mkvirtual <your env>`
2. Install django `pip install django`
3. Install django rest framework `pip install djangorestframework`
4. Install pygments for highlighting the code `pip install pygments`
5. Once that's done, clone or download this repository
6. Open command prompt (Windows) and activate the virtual environment `<your env>\Scripts\activate.bat`
7. And then change directory `cd <this repository>`
8. Make a migrations first `py manage.py migrate`
9. Optionaly, test the project if an error occurs `py manage.py test`
10. Run the project using `py manage.py runserver` and open up in browser `http://127.0.0.1:8000/`
11. In browsable API there's a 2 options, `User` and `Snippet` choose as you wish and then you can add snippet code in there
12. Before using schema, install the dependencies on your terminal `pip install coreapi pyyaml`
13. And then open up in browser with `http://127.0.0.1:8000/schema/` and there's auto-generated documentation about our snippet

**Test the API**
1. Create a superuser first `py manage.py createsuperuser`
2. And then go to `http://127.0.0.1:8000/admin/` so you can add a new data in `+Add` Snippet 
3. Open API `http://127.0.0.1:8000/snippet/`
4. Want to check detailed about the data just added 1-9 after `/snippet/`

**Progress Update**
1. Serializers (**done**)
2. Request and Response (**done**)
3. Authenticate (**done**)
4. Permissions (**done**)
5. Hyperlinked Relationship (**done**)
6. Pagination (**done**)
7. User Libraries (**on progress**)
8. Multiple Authenticate (not yet)

**Note**
1. For pagination is simple to use, go thoroughly in `DjangoAPI/settings.py` and then add : 

    `REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
    }`

**Explanations**
1. (I'll Added Later)

**Error**
1. So far, i got some error if user want to post a data in django administrator. I think it's because i didn't delete the database before and got
error `OperationalError at snippet/admin/`. The point is, when we will test our API for the first time, we create a superuser named Admin, and after the testings it's working,
we should remove the database and then make migrations to snippet and create 2 superuser for Admin and User again. (**fixed**)
2. The second error is `ImproperlyConfigured/user`, this happen (for my case) because when we will post a data we can choose that data belongs to user or the admin.
The functions is working but because i didn't delete database before so it's not working either LOL
3. Currently, CRUD in browsable API it's not showing so you must manually add a data in django administrator. (**fixed**)
4. Hyperlinked relationship it's not working, i believe there's a incorrect configured in `lookup_field` (**fixed**)
4. If there is anyone that willing to help me, just send a pull request

**Error Handling**
1. So, recently i have found a way to overcome the first error. I'm still not sure 100% if this completely fixed but i think so far so good. You just removed the previous database `db.sqlite3` and then delete all files in folder migrations except `__init__.py`, after that make a migrations for snippet `py manage.py makemigrations snippet` and run `py manage.py migrate`.At this point, create 2 super user again (user and admin) and open in browser `http://127.0.0.1:8000/admin` try to add data in Snippet then take a look in browsable API `http://127.0.0.1:8000/snippet/`

from django.contrib import admin
from api.models import UserList
# Register your models here.
admin.site.register(UserList)
admin.site.site_header = 'Administration'

from django.db import models

# Create your models here.
class UserList(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    content = models.TextField(max_length=1000, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

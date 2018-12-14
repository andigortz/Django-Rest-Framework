from django.db import models

# Create your models here.
class Post(models.Model):
    kind = models.CharField(max_length=150)
    starttime = models.DateTimeField(auto_now_add=True)
    endtime = models.DateTimeField(auto_now=True)
    station = models.CharField(max_length=100, unique=True)
    baseline = models.CharField(max_length=100, unique=True)
    event_type = models.CharField(max_length=50)
    reflector = models.BooleanField(default=True)

    def __str__(self):
        return self.kind

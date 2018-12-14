from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

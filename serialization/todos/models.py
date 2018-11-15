from django.db import models

# Create your models here.

class TodoList(models.Model):
	title = models.CharField(max_length=255, unique=True, null=False, blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	code = models.TextField()
	"""languages = models.CharField(choices=LANGUAGE_CHOICES, max_length=150, default='python')"""
	linenos = models.BooleanField(default=False)
	"""style = models.CharField(choices=STYLE_CHOICES, max_length=150, default='friendly')"""

	class Meta:
		ordering = ('created',)
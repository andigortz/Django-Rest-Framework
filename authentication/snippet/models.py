from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

# Create your models here.
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()

def save(self, *args, **kwargs):
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    super(Snippet, self).save(*args, **kwargs)
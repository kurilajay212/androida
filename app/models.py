from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Pat(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.TextField( max_length=100,default='Blank2')
    user_password = models.TextField( max_length=100,default='None')
    class Meta:
        ordering = ('user_name',)
class user(models.Model):
    author = models.ForeignKey(User)
    emailId  = models.EmailField(max_length=100)
    contact = models.IntegerField() 
    userName= models.CharField(max_length=50)
    password = models.CharField(max_length=50)

        
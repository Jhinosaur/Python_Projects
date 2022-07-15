from hashlib import md5
from django.db import models
import datetime
from django.utils import timezone
from django.forms import URLField
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Url(models.Model):
    link = models.URLField(max_length=250)
    uuid = models.CharField(max_length=10)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()




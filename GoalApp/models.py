from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class UserP(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.user.username

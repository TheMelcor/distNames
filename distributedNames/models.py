from __future__ import unicode_literals

from django.db import models


# Make models if needed here!


class Name(models.Model):
    name = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Node(models.Model):
    ip = models.TextField(max_length=15)
    isAuth = models.BooleanField


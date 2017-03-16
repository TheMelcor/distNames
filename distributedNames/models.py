from __future__ import unicode_literals

from django.db import models


# Make models if needed here!


class Name(models.Model):
    name = models.TextField(max_length=50)
    notFound = models.BooleanField(default=False)


class Node(models.Model):
    ip = models.TextField(max_length=15)
    notFound = models.BooleanField(default=False)


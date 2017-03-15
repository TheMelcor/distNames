from __future__ import unicode_literals

from django.db import models

from django.db import models

# Make models if needed here!


class Name:
    name = ''

    def __init__(self):
        return

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Node:
    ip = ""
    isAuthNode = False

    def __init__(self):
        return

    def set_ip(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip

    def set_auth(self, auth):
        self.isAuthNode = auth

    def get_auth(self):
        return self.isAuthNode

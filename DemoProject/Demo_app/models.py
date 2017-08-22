from __future__ import unicode_literals
from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)

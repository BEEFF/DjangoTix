from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=150, blank=False, default='')
    email = models.CharField(max_length=150, blank=False, default='')
    day = models.CharField(max_length=200,blank=False, default='')
    checkedin = models.BooleanField(default=False)

"""
This is Models in Barcode Server!

If you update or refactoring about database, Rewrite this!
"""
from django.db import models
from django.contrib.auth.models import User as U

# Create your models here.


class User(models.Model):
    '''
    Title : User

    This is User table extends admin user in django

    Attributes:
        user (Djang admin User) : This is One To One Filed to connect user in django
    '''
    user = models.OneToOneField(U, on_delete=models.CASCADE)


class Result(models.Model):
    '''
    Title : Result

    This is Result of recogniztion image

    Attributes:
        user (Djang admin User) : This is One To One Filed our user
        recognized (boolean) : This is boolean about recognition
        udi (string) : This is UDi barcode data
        img_path (string) : THis is img path
    '''
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dates = models.DateTimeField(auto_now_add=True)
    recognized = models.BooleanField(default=False)
    udi = models.CharField(max_length=300, default="NOT FOUND")
    img_path = models.CharField(max_length=300, null=True)

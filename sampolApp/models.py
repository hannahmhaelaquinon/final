from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import AutoField, EmailField
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.



class User(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    Uname = models.CharField(max_length=20, null=True)
    Pass = models.CharField(max_length=20, null=True)
    email = models.EmailField()

    class meta:
        db_table = 'user'

class Registrations(models.Model):
    ID_Number = models.IntegerField()
    fName = models.CharField(max_length = 20)
    plateNum = models.CharField(max_length = 20)
    vType = models.CharField(max_length = 20)

    class meta:
        db_table = 'registration'

class Admin(models.Model):
    admin_name =models.CharField(max_length = 20)
    admin_email = models.CharField(max_length = 20)
    admin_pass =models.CharField(max_length = 20)

    class meta:
        db_table = 'admin'

        
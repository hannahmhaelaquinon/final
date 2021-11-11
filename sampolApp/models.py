from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import AutoField
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class Registration(models.Model):
    student_id = models.AutoField(primary_key = True)
    sName = models.CharField(max_length = 255)
    plateNum = models.IntegerField()
    vType = models.CharField(max_length = 1000)
    

    class meta:
        db_table = 'register'
    def __str__(self):
        return self.student_id
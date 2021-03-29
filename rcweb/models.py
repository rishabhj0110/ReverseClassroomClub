from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save

# Create your models here.
class SignUp(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    pemail=models.EmailField(max_length=254)
    descr=models.CharField(max_length=1000)
    year=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    college=models.CharField(max_length=300)
    link=models.URLField(max_length=300)
    utype=models.CharField(max_length=150)


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=150)
    pemail=models.EmailField(max_length=254)
    college=models.CharField(max_length=250)
    degree=models.CharField(max_length=150)
    year=models.CharField(max_length=150)
    address=models.CharField(max_length=500)
    desc=models.CharField(max_length=1000)
    link=models.URLField(max_length=500)
    utype=models.CharField(max_length=150)
    def __str__(self):  # __str__
        return (self.user.username)

class Newsletter(models.Model):
    email=models.CharField(max_length=200)

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    sub=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)

class Instructor(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=150)
    desc=models.CharField(max_length=1000)
    qual=models.CharField(max_length=1000)
    link=models.URLField(max_length=500)

class Workshop(models.Model):
    etitle=models.CharField(max_length=200)
    edesc=models.CharField(max_length=1000)
    edoclink=models.URLField(max_length=500)
    einame=models.CharField(max_length=200)
    eidesc=models.CharField(max_length=1000)
    eilink=models.URLField(max_length=500)
    edate=models.CharField(max_length=150) 
    etime=models.CharField(max_length=150)
    eapply=models.URLField(max_length=500)

class Courses(models.Model):
    ctitle=models.CharField(max_length=200)
    cdesc=models.CharField(max_length=1000)
    cdoclink=models.URLField(max_length=500)
    ciname=models.CharField(max_length=200)
    cidesc=models.CharField(max_length=1000)
    cilink=models.URLField(max_length=500)
    csdate=models.CharField(max_length=150)
    cedate=models.CharField(max_length=150)
    ctime=models.CharField(max_length=150)
    capply=models.URLField(max_length=500)

class Ngo(models.Model):
    ngoname=models.CharField(max_length=200)
    ngodetails=models.CharField(max_length=1000)
    ntitle=models.CharField(max_length=200)
    ndesc=models.CharField(max_length=1000)
    ndoclink=models.URLField(max_length=500)
    niname=models.CharField(max_length=200)
    nidesc=models.CharField(max_length=1000)
    nilink=models.URLField(max_length=500)
    nsdate=models.CharField(max_length=150)
    nedate=models.CharField(max_length=150)
    ntime=models.CharField(max_length=150)
    napply=models.URLField(max_length=500)
    
class Emailsystem(models.Model):
    email=models.CharField(max_length=200)
    sub=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)
    time=models.CharField(max_length=150)
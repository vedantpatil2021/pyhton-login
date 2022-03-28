from datetime import datetime
import email
from unicodedata import name
from django.db import models

# Create your models here.

class EventRegistration(models.Model):
    eventname = models.CharField(max_length=300)
    eventdesc = models.TextField(max_length=1000)
    eventfromdate = models.DateField()
    eventtodate = models.DateField()
    eventfromtime = models.TimeField()
    eventtotime = models.TimeField()
    eventmode = models.CharField(max_length=200)
    eventhost = models.CharField(max_length=300)
    eventvenue = models.TextField(max_length=1000)
    eventnoattendees = models.CharField(max_length=200)
    eventcontactname = models.CharField(max_length=100)
    eventcontactemail = models.CharField(max_length=200)
    eventcontactphoneno = models.CharField(max_length=200)
    eventposter = models.ImageField(null=True, blank=True)
    eventadposter = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=500)
    userid = models.CharField(max_length=120)
    def __str__(self):
        return self.id


class GeneralDetails(models.Model):
    username = models.CharField(max_length=200)
    firstname =models.CharField(max_length=200)
    lastname =models.CharField(max_length=200)
    gender =models.CharField(max_length=200)
    phonenumber =models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob = models.DateField()
    fathername = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    state = models.CharField(max_length=500)
    district = models.CharField(max_length=200)
    alternameemail = models.CharField(max_length=200)
    whatsappnumber = models.CharField(max_length=50)
    institutename = models.CharField(max_length=150)
    instituteweblink = models.CharField(max_length=150)
    instituteaddress = models.CharField(max_length=700)
    institutecity = models.CharField(max_length=150)
    institutedstate = models.CharField(max_length=150)
    institutedistrict = models.CharField(max_length=150)
    instituteemail = models.CharField(max_length=150)
    institutetype = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)

    def __str__(self):
        return self.username



class AuditoriumData(models.Model):
    audiname = models.CharField(max_length=500)
    audiaddress = models.CharField(max_length=400)
    audicapacity = models.CharField(max_length=50)




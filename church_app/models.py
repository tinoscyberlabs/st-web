from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Event_Details_Model(models.Model):
    event_name = models.CharField(max_length=500)
    organizer = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    time = models.TimeField()
    cost = models.IntegerField()
    main_image = models.ImageField(upload_to='images/')
    event_description = models.CharField(max_length=1000)
    description_image = models.ImageField(upload_to='images/')
    event_venue = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    event_gallery_image = models.ImageField(upload_to='images/')

    def is_active(self):
        return self.end_date >= timezone.now()

    # def __str__(self):
    #     return f"{self.event_name} | {self.organizer} | {self.start_date} | {self.end_date} | {self.time} | {self.cost} | {self.main_image} | {self.event_description} | {self.description_image} | {self.event_venue} | {self.address} | {self.email} | {self.phone} | {self.event_gallery_image}"


class Event_Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    event_name = models.ForeignKey(Event_Details_Model,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MinistriesModel(models.Model):
    mass_times = models.ImageField(upload_to='images/')
    ask_for_prayer = models.ImageField(upload_to='images/')
    obitury = models.ImageField(upload_to='images/')


class Daily_Mass(models.Model):
    mass_days = models.CharField(max_length=100)
    mass_date = models.DateField()
    mass_time = models.TimeField()
    end_time  = models.TimeField()
    mass_description = models.CharField(max_length=1000)
    def __str__(self):
        return self.mass_days


class Special_Masses(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.event_name

class Obituary_Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Gallery_Model(models.Model):
    gallery_image = models.ImageField(upload_to='images/')


class Blog_Model(models.Model):
    blog_image = models.ImageField(upload_to='images/')
    date = models.DateField()

class Blog_News_Model(models.Model):
    blog_image = models.ImageField(upload_to='images/')
    date = models.DateField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.description


from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from json import load

MUNICIPE_CHOICES=[]

def fill_p():
    PROVINCE_CHOICES=[]
    with open('provincias-cidades.json') as f:
        data = load(f)
        for t in data:
            PROVINCE_CHOICES.append(tuple((t['name'], t['name'])))
        PROVINCE_CHOICES = tuple(PROVINCE_CHOICES) 
    return PROVINCE_CHOICES

def fill_m():
    MUNICIPE_CHOICES=[]
    with open('provincias-cidades.json') as f:
        data = load(f)
        return data

GROUP_CHOICES = (
    ('A+','A+'),
    ('AB+', 'AB+'),
    ('B+','B+'),
    ('O+','O+'),
    ('A-','A-'),
    ('AB-', 'AB-'),
    ('B-','B-'),
    ('O-','O-'),
)
PROVINCE_CHOICES=fill_p()
# Create your models here.
class Message(models.Model):
    dest = models.CharField(max_length=9)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # send(body='kkkk',to='947221912')
        return super().save(*args, **kwargs)
    
class Donor(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    group = models.CharField(max_length=50, choices=GROUP_CHOICES, default="A+")
    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES, default="Bengo")
    municipe = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.name
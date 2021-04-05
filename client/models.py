from django.db import models

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

class Donor(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    group = models.CharField(max_length=5, choices=GROUP_CHOICES, default="A+")
    province = models.CharField(max_length=100)
    municipe = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
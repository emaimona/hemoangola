from django.contrib import admin
from .models import Message, Donor

# Register your models here.
admin.site.register(Message)
admin.site.register(Donor)
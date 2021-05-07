from django.contrib import admin
from .models import Message, Donor

class DonorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'group', 'province', 'municipe', 'district', 'username', 'password']
    
    
# Register your models here.
admin.site.register(Message)
admin.site.register(Donor, DonorAdmin)
from django.contrib import admin
from .models import Lawyer

@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ['user','name','name_en','email_address','phone']
    list_display_link = ['name']

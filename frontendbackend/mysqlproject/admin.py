from django.contrib import admin
from .models import *

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model='Messages'
        fields='__all__'
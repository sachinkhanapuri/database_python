from django.db import models

# Create your models here.
class MessagesTb(models.Model):
    message=models.CharField(max_length=50)



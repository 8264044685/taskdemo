from django.db import models

# Create your models here.

status = [
    ('active', 'ACTIVE'),
    ('inactive', 'INACTIVE'),
    
]

class TaskData(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state=models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.IntegerField()
    status = models.CharField(choices=status, max_length=50, null=True, blank=True , default='active')












    
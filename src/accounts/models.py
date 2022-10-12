
from django.db import models
from django.contrib.auth.models import AbstractUser




DEPARTMAN = [
    ('Muhasebe','Muhasebe'),
    ('Satın Alma','Satın Alma'),
]

class CustomUser(AbstractUser):
    mygroup = models.CharField(max_length=50, choices=DEPARTMAN )
    
    
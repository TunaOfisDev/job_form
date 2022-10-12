
from django.db import models
from django.contrib.auth.models import AbstractUser




DEPARTMAN = [
    ('Arge','Arge'),
    ('Muhasebe','Muhasebe'),
    ('Satın Alma','Satın Alma'),
    ('Üretim','Üretim'),
    ('Planlama','Planlama'),
]

class CustomUser(AbstractUser):
    mygroup = models.CharField(max_length=50, choices=DEPARTMAN )
    
    
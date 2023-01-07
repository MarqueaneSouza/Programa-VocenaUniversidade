from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model): #A nossa classe Post é uma subclasse de Model - Post herda de Model (relação de herança)
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now())
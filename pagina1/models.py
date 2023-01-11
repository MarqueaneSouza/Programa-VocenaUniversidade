from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #A nossa classe Post é uma subclasse de Model - Post herda de Model (relação de herança)
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(default=timezone.now())

    def __str__(self): #método retorna o título do Post (django-admin): Post object -> Primeiro post
        return self.titulo
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    #para criar um opção de analize antes da publicação do post, temos um lista de opções de Status
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    
    titulo = models.CharField(max_length=250)
    
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, 
                                on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default='rascunho')


    #ordena a lista de post o mais recente primeiro, utilizando o sinal de '-' antes da lista
    class Meta:
        ordering = ('-publicado',)

    #para alterar o nome de exibição do post
    def __str__(self):
        return '{} - {}'.format(self.titulo, self.slug)                            



# Create your models here.

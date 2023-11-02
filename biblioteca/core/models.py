from django.db import models

class LivroModel(models.Model):

    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('Editora', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.PositiveIntegerField('ISBN', unique=True)  
    numero_paginas = models.PositiveIntegerField('Número de Páginas')  
    ano_escrita = models.PositiveSmallIntegerField('Ano da Obra')  

    def __str__(self):
        return self.titulo

from django.db import models

class LivroModel(models.Model):

    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('Editora', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('Isbn', max_length=200)
    numero_paginas = models.CharField('Número de Páginas', max_length=200)
    ano_escrita = models.CharField('Ano da Obra', max_length=200)

    def __str__(self):
        return self.titulo

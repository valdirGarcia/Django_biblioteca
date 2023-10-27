from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos dez caracteres')


class LivroForm(forms.ModelForm):
    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'numero_paginas', 'ano_escrita']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe o ISBN do livro."),
            },
            'numero_paginas': {
                'required': ("Informe o número de páginas do livro."),
            },
            'ano_escrita': {
                'required': ("Informe o ano de escrita do livro."),
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        # Adicione 
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        # Adicione
        return isbn

    def clean_numero_paginas(self):
        numero_paginas = self.cleaned_data['numero_paginas']
        # Adicione 
        return numero_paginas

    def clean_ano_escrita(self):
        ano_escrita = self.cleaned_data['ano_escrita']
        # Adicione 
        return ano_escrita

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data


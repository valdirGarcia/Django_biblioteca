from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_titulo_e_editora(value):
    if len(value) < 3:
        raise ValidationError('Deve ter pelo menos três caracteres')
    
def validate_autor(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos 10 caracteres')
    
def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError('Deve ter exatos 13 caracteres númericos')
    
def validate_numero_paginas(value):
    if len(value) < 3:
        raise ValidationError('Deve pelo menors 3 caraccteres númericos')
    
def validate_ano_escrita(value):
    if len(value) != 4:
        raise ValidationError('Deve ter exatos 4 caracteres númericos')




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
        validate_titulo_e_editora(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_titulo_e_editora(editora)
        return editora

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn

    def clean_numero_paginas(self):
        numero_paginas = self.cleaned_data['numero_paginas']
        validate_numero_paginas(numero_paginas)
        return numero_paginas

    def clean_ano_escrita(self):
        ano_escrita = self.cleaned_data['ano_escrita']
        validate_ano_escrita(ano_escrita)
        return ano_escrita

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data


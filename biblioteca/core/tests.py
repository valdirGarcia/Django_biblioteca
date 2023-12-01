from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus
from .models import LivroModel
from .forms import LivroForm
from django.urls import reverse


class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class IndexPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('core:index'))
        self.resp2 = self.client.post(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.FOUND)
        self.assertEqual(self.resp2.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp2, 'index.html')


class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):  
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 9),
            ('<br>', 9),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostOk(TestCase):
    def setUp(self):
        data = {
            'titulo': 'Contos de Machado de Assis',
            'editora': 'editora Brasil',
            'autor': 'Machado de Assis',  
            'isbn': 1234567890123,    
            'numero_paginas': 200,    
            'ano_escrita': 1899      
        }
        
        self.resp = self.client.post(r('core:cadastro'), data, follow=True)
        self.resp2 = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_status_code(self): 
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
        self.assertEqual(self.resp2.status_code , HTTPStatus.OK)

    def test_dados_persistidos(self): 
        self.assertTrue(LivroModel.objects.exists())

    def test_found_html(self):  
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostFail(TestCase):
    def setUp(self):
        data = {'titulo': 'Livro sem editora',}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_dados_persistidos(self):
        self.assertFalse(LivroModel.objects.exists())


class ListarGet_withoutBook_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_withoutBook_Test(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarGet_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='Editora Brasil',
            autor='Machado de Assis',
            isbn='1234567890123',
            numero_paginas=200,
            ano_escrita=1899
        )
        self.livro.save()
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self): 
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 10),
            ('Contos de Machado de Assis', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1234567890123',
            numero_paginas=200,
            ano_escrita=1899
        )
        self.livro.save()
        data = {'livro_id': self.livro.pk}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Contos de Machado de Assis', 1),
            ('<br>', 16),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LivroModelModelTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1234567890123',
            numero_paginas=200,
            ano_escrita=1899
        )
        self.livro.save()

    def test_created(self):
        self.assertTrue(LivroModel.objects.exists())


class LivroFormTest(TestCase):
    def test_fields_in_form(self):
        form = LivroForm()
        expected = ['titulo', 'editora', 'autor', 'isbn', 'numero_paginas', 'ano_escrita']
        self.assertSequenceEqual(expected, list(form.fields))
    
    
    def test_form_all_OK(self):
        dados = {
            'titulo': 'Contos do Machado de Assis',
            'editora': 'Editora Brasil',
            'autor': 'Machado de Assis',
            'isbn': '1234567890123',
            'numero_paginas': '200',
            'ano_escrita': '1880'
        }
        form = LivroForm(dados)
        errors = form.errors
        self.assertEqual({}, errors)
        
    def test_form_without_data_1(self):
        dados = dict(titulo='Contos do Machado de Assis')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Informe a editora do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_2(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Informe o título do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_3(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['isbn']
        msg = 'Informe o ISBN do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_4(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['numero_paginas']
        msg = 'Informe o número de páginas do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_5(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['ano_escrita']
        msg = 'Informe o ano de escrita do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_6(self):
        dados = dict(editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['autor']
        msg = 'Informe o autor do livro.'
        self.assertEqual([msg], errors_list)
    
    def test_form_less_than_3_character_1(self):   
        dados = dict(titulo='12', editora='Editora Brasil')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'título deve ter pelo menos três caracteres'
        self.assertEqual([msg], errors_list)
    
    def test_form_less_than_3_character_2(self):  
        dados = dict(titulo='Contos do Machado de Assis', editora='12')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['editora']
        msg = 'editora deve ter pelo menos três caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_10_character(self):  
        dados = dict(autor='valdir')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['autor']
        msg = 'Autor deve ter pelo menos 10 caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_13_numbers(self):  
        dados = dict(isbn='123456789')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['isbn']
        msg = 'O ISBN deve ter exatamente 13 dígitos'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_3_numbers(self):  
        dados = dict(numero_paginas='1000')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['numero_paginas']
        msg = 'O número de páginas deve ser um valor entre 1 e 999'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_4_numbers(self):  
        dados = dict(ano_escrita='12345')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['ano_escrita']
        msg = 'O ano da obra deve conter exatamente 4 dígitos numéricos'
        self.assertEqual([msg], errors_list)

    def test_current_year(self):  
        dados = dict(ano_escrita='3000')
        form = LivroForm(dados)
        errors = form.errors                            
        errors_list = errors['ano_escrita']
        msg = 'O ano de escrita não pode ser posterior ao ano atual'
        self.assertEqual([msg], errors_list)


class LivroDeletarTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1234567890123',
            numero_paginas=200,
            ano_escrita=1899
        )
        self.livro.save()  
        data = {'livro_id': self.livro.pk}
        self.resp = self.client.post(r('core:deletar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_livro_excluido_do_banco(self):
        livro_exists = LivroModel.objects.filter(pk=self.livro.pk).exists()
        self.assertFalse(livro_exists)  
    

class LivroAtualizarTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1234567890123',
            numero_paginas=200,
            ano_escrita=1899
        )
        self.livro.save()  

        data = {
            'livro_id': self.livro.pk,
            'titulo': 'Novo Título',
            'editora': 'Nova Editora',
            'autor': 'Novo Autor',
            'isbn': '9876543210987',
            'numero_paginas': 250,
            'ano_escrita': 1900
        }
        self.resp = self.client.post(reverse('core:atualizar'), data,follow=True)

    def test_status_code(self):
         self.assertEqual(self.resp.status_code, HTTPStatus.OK)

    def test_livro_atualizado_no_banco(self):
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, 'Novo Título')
        self.assertEqual(self.livro.editora, 'Nova Editora')
        self.assertEqual(self.livro.autor, 'Novo Autor')
        self.assertEqual(str(self.livro.isbn), '9876543210987')  
        self.assertEqual(self.livro.numero_paginas, 250)
        self.assertEqual(self.livro.ano_escrita, 1900)

    
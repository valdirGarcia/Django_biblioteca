# Projeto Biblioteca

Este projeto foi idealizado durante o curso de Desenvolvimento Web 3 na Fatec Araras. Ele se baseia em uma aplicação Django pré-existente, que estamos aprimorando na segunda fase do projeto, com um foco especial em Desenvolvimento Orientado a Testes (TDD).

## Objetivo
O objetivo principal deste projeto é aprimorar uma aplicação de biblioteca existente, implementando novos recursos, melhorias de desempenho e, ao mesmo tempo, aprofundar nossos conhecimentos em Desenvolvimento Orientado a Testes. O TDD desempenha um papel central neste projeto, permitindo-nos construir e aprimorar funcionalidades com maior confiabilidade e qualidade.

## Como Rodar em Sua Máquina

No ambiente Linux:

```console
git clone https://github.com/valdirGarcia/Django_biblioteca.git
cd django_biblioteca/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd biblioteca/
python manage.py runserver
```

No ambiente Windows:

```console
git clone https://github.com/valdirGarcia/Django_biblioteca.git
cd django_biblioteca/
virtualenv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd biblioteca/
python manage.py runserver

```

No momento, a aplicação permite apenas a realização de cadastros (create) e consultas (read) de livros registrados. Para acessar o site, basta copiar o código gerado pelo comando 'runserver' e colá-lo no seu navegador de preferência.

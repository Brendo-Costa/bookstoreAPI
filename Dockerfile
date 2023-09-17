# syntax=docker/dockerfile:1

#Imagem do python usada na criação da imagem da aplição
FROM python:3.8-slim-buster

WORKDIR /app


# Variável de Ambiente
#ENV python manage.py runserver

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libpq-dev python-dev libssl-dev build-essential

# Copiar para = Copiar de

RUN pip install --upgrade pip
# Rodando comendos:
# 1. Instalando 
RUN pip install -r requirements.txt

RUN pip install psycopg2

RUN pip install psycopg2-binary
# Copie
# DE: pasta raiz, onde arquivo Dockerfile está.
# PARA: pasta (WORKDIR) criada no container
COPY . .

RUN python manage.py makemigrations

#Permissão para executar o arquivo .sh
RUN ["chmod", "+x", "./docker.sh"]

EXPOSE 8000

#Após o container levantado, rode o arquivo docker.sh
CMD ["/bin/bash", "-c", "./docker.sh"]
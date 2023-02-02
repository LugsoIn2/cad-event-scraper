# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
 && sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen \
 && locale-gen

RUN apt-get install -y curl
RUN apt-get install -y jq

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src ./src
COPY main.py main.py

CMD [ "python3", "./main.py"]
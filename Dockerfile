# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# RUN apt-get update && \
#     apt-get install -y locales && \
#     sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \
#     dpkg-reconfigure --frontend=noninteractive locales
# 
# ENV LANG de_DE.UTF-8
# ENV LC_ALL de_DE
RUN apt-get update && \
    apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
 && sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen \
 && locale-gen


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "./main.py"]
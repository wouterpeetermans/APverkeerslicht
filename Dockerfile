FROM php:8.2.11-apache

WORKDIR /var/www/html/

COPY index.php .
COPY groennaarrood.py .
COPY oranje-knipperen.py .
COPY roodnaargroen.py .

RUN apt update
RUN apt install -y python3 python3-paho-mqtt psmisc


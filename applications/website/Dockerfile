FROM composer:2.2.4 AS composer

FROM php:8.1-fpm

COPY . /var/www/html

RUN apt-get update -y
RUN apt-get -y install gcc make autoconf libc-dev pkg-config libzip-dev

WORKDIR /var/www/app

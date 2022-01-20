FROM nginx:1.15-alpine

RUN apk update
RUN apk add openssl

RUN rm -f /etc/nginx/conf.d/*
RUN mkdir /certs/
RUN mkdir /www

COPY index.html /www/index.html
COPY default.conf /etc/nginx/conf.d/default.conf

COPY request.crt /certs
COPY request.key /certs

#RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /certs/selfsigned.key -out /certs/selfsigned.crt -subj "/C=CH/ST=Vaud/L=Lausanne/O=server/OU=server/CN=server"
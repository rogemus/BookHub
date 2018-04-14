FROM nginx:latest@sha256:18156dcd747677b03968621b2729d46021ce83a5bc15118e5bcced925fb4ebb9
LABEL version="1.0"
LABEL maintainer="bookhub@corporation.com"

RUN mkdir /etc/nginx/snippets
COPY ./config/certs/* /etc/ssl/
COPY ./config/nginx.conf /etc/nginx/nginx.conf
COPY ./config/bookhub.com.conf /etc/nginx/conf.d/bookhub.com.conf
COPY ./config/snippets/* /etc/nginx/snippets/
CMD ["nginx", "-g", "daemon off;"]

FROM nginx
LABEL version="1.0"
LABEL maintainer="bookhub@corporation.com"

RUN mkdir /etc/nginx/snippets
COPY ./config/certs/* /etc/ssl/
COPY ./config/nginx.conf /etc/nginx/nginx.conf
COPY ./config/bookhub.com.conf /etc/nginx/conf.d/bookhub.com.conf
COPY ./config/snippets/* /etc/nginx/snippets/
CMD ["nginx", "-g", "daemon off;"]

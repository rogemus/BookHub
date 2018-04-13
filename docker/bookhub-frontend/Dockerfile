FROM node:8.11-slim
LABEL version="1.0"
LABEL maintainer="bookhub@corporation.com"


RUN mkdir /app
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build:prod
CMD cp -r /app/public/* /var/www/bookhub.com

FROM node:8.11-slim

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN npm install
RUN npm run build:prod
CMD cp -r /app/public/* /var/www/bookhub.com

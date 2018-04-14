FROM node:8.11-slim@sha256:9b10ed416b3e8dbebc2cf887fb9982f7f957b660d24afb4a8eff7c9254243b2b
LABEL version="1.0"
LABEL maintainer="bookhub@corporation.com"


RUN mkdir /app
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build:prod
CMD cp -r /app/public/* /var/www/bookhub.com

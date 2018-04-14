FROM node:8.11.1 as build-deps

# Stage 1 - the build process
WORKDIR /app

COPY package*.json yarn.lock ./

RUN npm install

COPY . .

RUN npm run build:prod


# Stage 2 - the production environment
FROM node:8.11.1-alpine

LABEL version "1.0"
LABEL maintainer "BookHub Corporation <technical@bookhub.com>"

WORKDIR /app

COPY --from=build-deps /app/public ./


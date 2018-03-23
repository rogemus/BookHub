FROM node:8.10-slim

ENV NPM_CONFIG_LOGLEVEL warn

COPY . /code/

WORKDIR /code/

ENV NODE_PATH=/node_modules

ENV PATH=$PATH:/node_modules/.bin

RUN npm install

RUN npm cache clean --force

CMD [ "yarn", "run", "dev:server"]

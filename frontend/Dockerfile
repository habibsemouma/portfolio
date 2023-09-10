FROM node:18-slim AS build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

ENTRYPOINT [ "npm","start" ]
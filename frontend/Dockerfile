FROM node:18-slim AS build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

FROM nginx:alpine AS deploy-static

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html

COPY --from=build /app/build .
ENTRYPOINT [ "nginx","-g","daemon off;" ]
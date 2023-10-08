FROM node:18-bullseye AS build
RUN apt-get update && apt-get install -y --no-install-recommends curl
ARG NPM_TOKEN
WORKDIR /usr/src/app
COPY . /usr/src/app/

RUN npm ci --omit=dev && \ 
    cp -R /usr/src/app/node_modules /usr/src/app/node_modules_prod && \
    npm ci && \
    npm run build && curl -sf https://gobinaries.com/tj/node-prune | sh

FROM node:20-alpine3.18
ENV NODE_ENV production
ENV PORT=80

USER node
WORKDIR /usr/src/app
COPY --chown=node:node --from=build /usr/src/app/node_modules_prod /usr/src/app/node_modules
COPY --chown=node:node --from=build /usr/src/app/build /usr/src/app/
COPY --chown=node:node --from=build /usr/src/app/package.json /usr/src/app/
COPY --chown=node:node ./static /usr/src/app/
CMD ["node", "index.js"]

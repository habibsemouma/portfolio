#!/bin/bash

docker build -t portfolio-frontend ./frontend
docker build -t retrocrypto ./retrocrypto
docker build -t ytbmp3 ./ytbmp3


konsole --noclose -e "docker run --rm --name retrocrypto --network portfolio  -p 4000:4000 retrocrypto "&
konsole --noclose -e "docker run --rm --name ytbmp3 --network portfolio  -p 3000:3000 ytbmp3"&
konsole --noclose -e "docker run --rm --name portfolio --network portfolio  -p 8080:80 portfolio-frontend"&

sleep 10
#!/bin/bash

(cd frontend && yarn install && yarn build)

docker-compose build --no-cache


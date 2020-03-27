#!/bin/bash
yarn install
yarn build
docker build --no-cache -t docker.pkg.github.com/mariolyon/students/students-frontend:latest .

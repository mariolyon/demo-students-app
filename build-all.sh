#!/bin/bash

(cd frontend && ./build.sh) && (cd backend && ./build.sh)

docker login docker.pkg.github.com -u mariolyon -p $GITHUB_TOKEN
docker push docker.pkg.github.com/mariolyon/students/students-backend
docker push docker.pkg.github.com/mariolyon/students/students-frontend

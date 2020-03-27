Students Rest API and simple React UI
=====================================

# Author
Mario Lyon

# Prerequisites
Node, Yarn, and Python3

# Running
```bash
docker login docker.pkg.github.com -u mariolyon -p $GITHUB_PACKAGE_READER_TOKEN
docker-compose up
```
This will pull the published students-backend and students-frontend dockers images from github.
This will run a docker container with the python flask server on port 5000,
and the react spa on port 3000.

You can access it by going to http://localhost:3000 in your web browser.


# Building and Deploying docker images
This shell script is to be executed whenever the docker images need to be republished
```bash
./build-all.sh
```

#!/bin/bash

echo "building docker"
docker build -t vlby . 

echo "run docker build"
docker run -it vlby
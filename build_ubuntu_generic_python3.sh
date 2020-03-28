#!/bin/bash

PYTHON_MAJOR=3
PYTHON_MINOR=7
PYTHON_MICRO=6

docker build -f dockerfile.ubuntu_generic_python3 \
       -t richarddally/ubuntu_generic_python3:$PYTHON_MAJOR.$PYTHON_MINOR.$PYTHON_MICRO \
       --build-arg PYTHON_MAJOR=$PYTHON_MAJOR \
       --build-arg PYTHON_MINOR=$PYTHON_MINOR \
       --build-arg PYTHON_MICRO=$PYTHON_MICRO \
       .

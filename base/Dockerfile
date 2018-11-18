# docker build -t ubuntu1604py27 .
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    && apt-get autoremove \
    && apt-get clean

RUN apt-get update

# update pip
RUN python -m pip install pip --upgrade
RUN python -m pip install wheel
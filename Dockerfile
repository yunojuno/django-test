FROM python:2.7

RUN apt-get update \
    && apt-get install vim -y

# Environment
ENV PYTHONUNBUFFERED 1

# Code
RUN mkdir /src
WORKDIR /src
RUN virtualenv /venv
ADD . /src/

# pip global
RUN /bin/bash -c "pip install -r requirements-tox.txt"

# pip virtualenv
RUN /bin/bash -c "source /venv/bin/activate \
    && pip install -r requirements.txt"

# Ports
EXPOSE 8000
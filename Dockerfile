FROM python:2.7

RUN apt-get update \
    && apt-get install vim -y

# Environment
ENV PYTHONUNBUFFERED 1

# Code
RUN mkdir /src
WORKDIR /src
RUN virtualenv /venv
RUN /bin/bash -c "source /venv/bin/activate"
ADD requirements.txt /src/
RUN /bin/bash -c "pip install -r requirements.txt"
ADD . /src/

# Ports
EXPOSE 8000
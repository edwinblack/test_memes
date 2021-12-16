# pull the official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies 
RUN apk update --no-cache add \
    g++ \
    libc6-compat \
    make \
    build-base \
    openblas-dev \
    unzip \
    cmake \
    curl \
    ca-certificates \
    libstdc++  \
    libxml2 \
    zip \
    libtbb  \
    lua5.2 \
    wget \
    cmake clang clang-dev make gcc g++ libc-dev linux-headers \
    boost-dev \
    && apk add --virtual build-deps gcc g++ python3-dev musl-dev
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
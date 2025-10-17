# pull official base image
FROM python:3.10.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

# install system dependencies
RUN apk update && apk --no-cache add \
    libressl-dev libffi-dev gcc musl-dev python3-dev openssl-dev cargo \
    nodejs npm

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy package files for npm install
COPY ./package.json ./
RUN npm install

# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
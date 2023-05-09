FROM alpine:3.17.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN set -ex \
    && apk update \
    && apk add curl gnupg gcc g++ git

#RUN apk --no-cache add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main firefox
RUN apk --no-cache add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing firefox
RUN apk --update add python3 py3-pip

# Copy in your requirements file
ADD requirements.txt /code/requirements.txt

RUN set -ex \
    && pip3 install --upgrade pip --ignore-installed packaging \
    && pip3 install --ignore-installed packaging  --no-cache-dir -r /code/requirements.txt

# Configuration for cron
RUN mkdir /cron
RUN touch /cron/django_cron.log
RUN apk add openrc --no-cache
RUN apk add busybox-openrc

COPY . /code

EXPOSE 80
EXPOSE 443
RUN ["chmod", "+x", "./docker-entrypoint.sh"]

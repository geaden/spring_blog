FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY . .

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements/local.txt --no-cache-dir && \
    apk --purge del .build-deps

RUN source init.sh
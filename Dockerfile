FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY . .

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements/local.txt --no-cache-dir && \
    python3 -m pip install -r requirements/staging.txt --no-cache-dir && \
    apk --purge del .build-deps
RUN apk add firefox

ENV MOZ_HEADLESS=1
ENV SECRET_KEY="$( cat secret.txt )"
ENV DJANGO_SETTINGS_MODULE=hotdot.settings.local
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app/hotdot/hotdot

RUN python3 hotdot/manage.py collectstatic
RUN python3 hotdot/manage.py migrate blog
RUN python3 hotdot/manage.py migrate tags

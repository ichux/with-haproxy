FROM python:3.10-bullseye as python-be

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

ENV P1="pip3 install --cache-dir . --disable-pip-version-check"

COPY requirements.txt .

RUN $P1 pip setuptools wheel && $P1 -r requirements.txt && \
find /usr/local/lib/python3.10 -name '__pycache__' -type d -print0 | xargs -0 /bin/rm -rf '{}' \
&& find /usr/local/lib/python3.10 -iname '*.pyc' -delete

FROM python:3.10-bullseye

COPY --from=python-be /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=python-be /usr/local/bin /usr/local/bin

WORKDIR /web

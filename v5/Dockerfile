FROM python:3.10.8-alpine3.16 as python-alpine

ENV P1="pip3 download --cache-dir . --only-binary=:all"
ENV P2="pip3 install --no-deps --find-links=. --cache-dir . --disable-pip-version-check"
ENV P3="pip3 install --find-links=. --cache-dir . --disable-pip-version-check"

COPY requirements.txt .
COPY wheels/*.whl .

RUN $P1 pip setuptools wheel && $P3 pip setuptools wheel && $P2 $(ls *.whl | tr '\n' ' ')
RUN $P1 -r requirements.txt && $P3 $(ls *.whl | tr '\n' ' ')  &> /dev/null && \
    find /usr/local/lib/python3.10 -name '__pycache__' -type d -print0 | xargs -0 /bin/rm -rf '{}' && \
    find /usr/local/lib/python3.10 -iname '*.pyc' -delete

FROM python:3.10.8-alpine3.16

COPY --from=python-alpine /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=python-alpine /usr/local/bin /usr/local/bin

RUN apk add --no-cache build-base

WORKDIR /web
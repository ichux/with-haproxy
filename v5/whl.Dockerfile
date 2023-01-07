FROM python:3.10.8-alpine3.16 as python-alpine

ENV P1="pip3 download --cache-dir . --only-binary=:all"
ENV P3="pip3 install --find-links=. --cache-dir . --disable-pip-version-check"

RUN apk add --no-cache build-base linux-headers
COPY requirements.txt .

RUN $P1 pip setuptools wheel -r requirements.txt && $P2 pip setuptools wheel && \
    $P2 $(ls *.gz | tr '\n' ' ') && $P2 $(ls *.whl | tr '\n' ' ')  &> /dev/null && \
    find /usr/local/lib/python3.10 -name '__pycache__' -type d -print0 | xargs -0 /bin/rm -rf '{}' && \
    find /usr/local/lib/python3.10 -iname '*.pyc' -delete

RUN mkdir whls && find wheels -name '*.whl' -exec install -c {} . \;  && mv *.whl whls

FROM python:3.10.8-alpine3.16

COPY --from=python-alpine /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=python-alpine /usr/local/bin /usr/local/bin
COPY --from=python-alpine /whls /wheels

RUN apk add --no-cache build-base

WORKDIR /web
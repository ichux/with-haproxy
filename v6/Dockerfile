FROM python:3.10.12-slim-bullseye AS builder

RUN apt update && apt install build-essential -y
RUN apt install -y curl python3-venv

WORKDIR /home

COPY requirements.txt .

RUN python3 -m venv .env && . .env/bin/activate && \
    pip install -U pip setuptools wheel && \
    pip install -r requirements.txt && \
    find . -name '__pycache__' -type d -print0 | xargs -0 /bin/rm -rf '{}' && \
    find . -iname '*.pyc' -delete

FROM python:3.10.12-slim-bullseye

COPY --from=builder /home/ /home/

WORKDIR /home/web/

# CMD tail -f /dev/null
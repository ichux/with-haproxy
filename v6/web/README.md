# How to run

```bash

cp .env.example .env # then change the port taste
make ba

curl -sX POST -F image=@path/to/an/image 'http://localhost:5000/'\
    | base64 -d > image2.png

# Then display image2.png in your image viewer

# RUN apk add --no-cache build-base linux-headers # && apk del build-base linux-headers && rm -rf /var/cache/apk/*
# pip freeze | grep -Ei "flask|pillow|gunicorn" > requirements.txt

```

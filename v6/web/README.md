# How to run

```bash

cp .env.example .env # then change the port taste
make ba

# depending on the image type uploaded, save it with such
curl -sX POST -F image=@/path/to/an/image http://localhost:8000/ | base64 -d > randomimage.png
curl -sX POST -F image=@/path/to/an/image http://localhost:8000/ | base64 -d > randomimage.jpeg

# Then display randomimage.png in your image viewer

# RUN apk add --no-cache build-base linux-headers # && apk del build-base linux-headers && rm -rf /var/cache/apk/*
# pip freeze | grep -Ei "flask|pillow|gunicorn" > requirements.txt

```

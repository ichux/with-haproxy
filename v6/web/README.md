# How to run

```shell
curl -sX POST -F image=@path/to/an/image 'http://localhost:5000/image'\
    | base64 -d > image2.png
# Then display image2.png in your image viewer
```

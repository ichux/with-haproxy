from base64 import encodebytes
from io import BytesIO

from flask import Flask, make_response, request
from PIL import Image

app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    return {"healthcheck": "UP"}


@app.route("/", methods=["POST"])
def upload():
    if (image := request.files.get("image")) is not None:
        image = Image.open(BytesIO(image.read()))
        buffer = BytesIO()
        image.save(buffer, format="PNG")

        return make_response(encodebytes(buffer.getvalue()).decode("ascii"), 200)
    else:
        return make_response("`image` field is required.", 400)


if __name__ == "__main__":
    app.run(debug=True)

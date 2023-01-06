import io

import numpy as np
from matplotlib import pyplot


def bufio():
    pyplot.figure()
    pyplot.plot([1, 2])
    pyplot.title("test")

    buffer = io.BytesIO()
    pyplot.savefig(buffer, format="png")
    pyplot.savefig("real.png", format="png")

    buffer.seek(0)
    data = buffer.read()
    buffer.close()

    with open("copy.png", "wb") as img:
        img.write(data)


def save_to():
    ys = 200 + np.random.randn(100)
    x = [x for x in range(len(ys))]
    pyplot.plot(x, ys, "-")
    pyplot.fill_between(x, ys, 195, where=(ys > 195), facecolor="g", alpha=0.6)
    pyplot.title("Sample Visualization")
    # pyplot.show()
    pyplot.savefig("points.png")


bufio()
save_to()

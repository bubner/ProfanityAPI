"""
ProfanityAPI WSGI server in Flask.
"""

from flask import Flask, request, abort, make_response
from profanity_check import predict, predict_prob
import opennsfw2 as n2
import uuid

app = Flask(__name__)

@app.route("/")
def f():
    text = request.args.get("f")
    if not text:
        abort(400)
    is_profane = bool(predict([text])[0])
    prob = predict_prob([text])[0]
    res = make_response({
        "text": text,
        "profane": is_profane,
        "probability": prob
    })
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res

@app.route("/img", methods=["POST"])
def g():
    img = request.data
    # Write into a file path
    rand_path = str(uuid.uuid4())
    with open(f"/tmp/{rand_path}.png", "wb") as f:
        f.write(img)
    prediction = n2.predict_image(f"/tmp/{rand_path}.png")
    res = make_response({
        "nsfw": prediction
    })
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


@app.route("/video", methods=["POST", "OPTIONS"])
def h():
    raise NotImplementedError("Video processing is not implemented yet.")

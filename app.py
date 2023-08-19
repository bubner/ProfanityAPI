"""
ProfanityAPI WSGI server in Flask.
"""

from flask import Flask, request, abort, make_response
from profanity_check import predict, predict_prob

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

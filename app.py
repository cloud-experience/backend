from checkPage import checkPage
from flask import Flask, request
from flask_restx import Api, Resource
from flask_cors import CORS, cross_origin

TARGET_WORDS = [
    "바카라",
    "카지노",
    "파워볼",
    "사다리",
    "슬롯",
    "카지노",
    "홀짝",
    "블랙잭",
    "홀덤",
    "잭팟",
    "오피",
    "출근부",
    "야동",
    "이용약관",
]


app = Flask("checkPageAPI")
CORS(app)
api = Api(app)


@api.route("/check/<string:url1>/<string:url2>")
class main(Resource):
    def get(self, url1, url2):
        url = f"{url1}/{url2}"
        data = checkPage(url, TARGET_WORDS)
        return data


app.run(host="0.0.0.0", port=80)
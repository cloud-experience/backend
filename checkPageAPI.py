from checkPage import checkPage
from flask import Flask, request
from flask_restx import Api, Resource

TARGET_WORDS = ["바카라", "카지노", "이용약관"]


app = Flask("checkPageAPI")
api = Api(app)


@api.route("/check/<string:url1>/<string:url2>")
class main(Resource):
    def get(self, url1, url2):
        url = f"{url1}/{url2}"
        data = checkPage(url, TARGET_WORDS)
        return data


app.run(host="0.0.0.0", port=6000)

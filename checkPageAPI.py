from checkPage import checkPage
from flask import Flask, request
from flask_restx import Api, Resource

TARGET_WORDS = ["바카라", "카지노", "이용약관"]
ADDR = "https://bit.ly/334DlJS"


# def main():
#     count = checkPage(ADDR, TARGET_WORDS)
#     print(f"찾은 유해 단어 개수 : {count}")


# main()

app = Flask("checkPageAPI")
api = Api(app)

# @app.route("/<addr>")
# def main(addr):
#     ADDR = f"https://{addr}"
#     print(f"connect to {ADDR}")
#     count = checkPage(ADDR)
#     return str(count)


@api.route("/")
class test(Resource):
    def get(self):
        return {"spam": True}


app.run(host="localhost", port=6000)

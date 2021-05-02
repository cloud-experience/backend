from checkPage import checkPage
from flask import Flask, request

TARGET_WORDS = ["바카라", "카지노", "이용약관"]
app = Flask("checkPageAPI")

# ADDR = "https://www.naver.com"


# def main():
#     count = checkPage(ADDR, TARGET_WORDS)
#     print(f"찾은 유해 단어 개수 : {count}")


# main()


@app.route("/<addr>")
def main(addr):
    ADDR = f"https://{addr}"
    print(f"connect to {ADDR}")
    count = checkPage(ADDR)
    return str(count)


app.run(host="localhost", port=6000)

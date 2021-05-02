from checkPage import checkPage
from flask import Flask

app = Flask("checkPageAPI")

ADDR = "https://www.naver.com"


def main():
    count = checkPage(ADDR)
    print(f"찾은 유해 단어 개수 : {count}")


main()

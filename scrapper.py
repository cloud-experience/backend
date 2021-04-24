import requests
from bs4 import BeautifulSoup


def conn(URL):
    r = requests.get(URL)
    print(r.status_code)


def main():
    conn("https://www.naver.com")


main()
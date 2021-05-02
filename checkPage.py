import requests
from bs4 import BeautifulSoup

TARGET = ["바카라", "카지노", "이용약관"]


def conn(URL):
    r = requests.get(URL)
    if r.status_code == 200:
        print(f"{URL} CONNECTED")
    else:
        print(f"ERROR CODE : {r.status_code}")
    return r.text


def extractString(data):
    soup = BeautifulSoup(data, "html.parser")
    words = soup.find_all("a")
    return words


def checkString(words):
    count = 0
    for word in words:
        if word.string in TARGET:
            count += 1
        # print(f"{word.string} : {count}")
    return count


def checkPage(URL):
    data = conn(URL)
    words = extractString(data)
    count = checkString(words)
    return count

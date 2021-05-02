import requests
from bs4 import BeautifulSoup


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


def checkString(words, TARGET_WORDS):
    count = 0
    for word in words:
        if word.string in TARGET_WORDS:
            count += 1
        # print(f"{word.string} : {count}")
    return count


def checkPage(URL, TARGET_WORDS):
    data = conn(URL)
    words = extractString(data)
    count = checkString(words, TARGET_WORDS)
    return count

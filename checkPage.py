import requests
from bs4 import BeautifulSoup
from checkDB import searchDB, newData, updateDB


def unshortenURL(URL):
    print(f"원본 URL : {URL}")
    URL = f"https://{URL}"
    session = requests.Session()  # so connections are recycled
    r = session.head(URL, allow_redirects=True)
    return r.url


def conn(URL):
    print(f"실제 URL : {URL}")
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
    URL = unshortenURL(URL)
    DBdata = searchDB(URL)
    if DBdata == ():  # DB에 저장된 데이터가 없으면(최초검색)
        data = conn(URL)
        words = extractString(data)
        count = checkString(words, TARGET_WORDS)
        try:
            newData("'" + URL + "'", count)
        except:
            print("DB작성 에러")
        data = {
            "redirectedURL": URL,
            "word_count": count,
            "first_date": "FIRST DISCOVERED",
            "last_date": "",
            "hits": 1,
        }
    else:  # DB에 데이터가 존재하는 경우
        updateDB(URL)  # 마지막 조회 날짜 업데이트
        data = {
            "redirectedURL": DBdata[0][0],
            "word_count": DBdata[0][1],
            "first_date": DBdata[0][2].isoformat(),
            "last_date": DBdata[0][3].isoformat(),
            "hits": DBdata[0][4],
        }
    return data

import pymysql

RDS_ENDPOINT = "database-2.cnr20hoyd3cu.ap-northeast-2.rds.amazonaws.com"
RDS_PORT = 3306
RDS_USER = "admin"
RDS_PASSWORD = "password"
RDS_DATABASE = "mydb"
RDS_TABLE = "spamlist"

# RDS Connect start
conn = pymysql.connect(
    host=RDS_ENDPOINT,
    port=RDS_PORT,
    user=RDS_USER,
    password=RDS_PASSWORD,
    db=RDS_DATABASE,
)


def searchDB(url):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {RDS_TABLE} WHERE url = %s", url)
    result = cur.fetchall()
    cur.close()
    return result


def newData(url, count):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {RDS_TABLE}(url,word_count) VALUES ({url},{count})")
    conn.commit()
    cur.close()


def updateDB(url):
    cur = conn.cursor()
    cur.execute(f"UPDATE spamlist SET last_date = NOW() WHERE url = %s", url)
    cur.execute(f"UPDATE spamlist SET hits = hits+1 WHERE url = %s", url)
    conn.commit()
    cur.close()

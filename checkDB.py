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
    return result


def newDB(url, count):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {RDS_TABLE}(url,word_count) VALUES ({url},{count})")
    conn.commit()


def updateDB(url):
    cur = conn.cursor()
    cur.excute(f"UPDATE table SET date = GETDATE() where url = %s", url)
    conn.commit()
"""

"""
import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='loki',
                                  charset='utf8')
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def register(self, username, passwd):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [username])
        result = self.cur.fetchone()
        if result:
            print("该用户已存在")
            return
        try:
            sql = "insert into user (name,passwd) values (%s,%s);"
            self.cur.execute(sql,[username,passwd])
            self.db.commit()
            print("注册成功")
        except Exception as e:
            self.db.rollback()
            print(e)

if __name__ == '__main__':
    db = Database()
    db.register("name","passwd")
    db.close()


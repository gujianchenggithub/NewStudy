import pymysql
from pymysql import connect
from file import data1
import logging
logging.getLogger().setLevel(logging.INFO)


class operateDb():

    # def __init__(self, host, port, user, passwd, db, charset='utf8'):
    #     self.host = host
    #     self.port=port
    #     self.user = user
    #     self.passwd=passwd
    #     self.db=db
    #     self.charset=charset

    def connet(self):

        self.conn = pymysql.connect(host=data1.host,
                        port = 3306,
                        user= 'root',
                       passwd='',
                       db='empirecms',
                       charset='utf8')
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self,sql):
        res=None
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
            # res=self.cursor.fetchmany(100)

            logging.info("查询--->>>" + sql + "<<<---成功！！")
            logging.info(res)
            # print(res)
            self.close()
        except Exception as e:
            print(e)
        return res

    def get_all(self,sql):
        res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
            logging.info("查询--->>>" + sql + "<<<---成功！！")
            logging.info(res)
            self.close()
        except Exception as e:
            print(e)
        return res

    #插入数据
    def insert(self, sql):

        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            logging.info("插入数据" + sql + "成功！！")
            self.conn.commit()
            self.close()
        except Exception as e:
            logging.info(e)
            logging.info("插入 " + sql + " 执行失败！！")
            self.conn.rollback()
        return count

    def delete(self, sql):

        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            logging.info("删除数据" + sql + "成功！！")
            self.conn.commit()
            self.close()
        except Exception as e:
            logging.info(e)
            logging.info("删除 " + sql + " 执行失败！！")
            self.conn.rollback()
        return count

    def update(self, sql):

        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            logging.info("更新数据" + sql + "成功！！")
            self.conn.commit()
            self.close()
        except Exception as e:
            logging.info(e)
            logging.info("更新 " + sql + " 执行失败！！")
            self.conn.rollback()
        return count



































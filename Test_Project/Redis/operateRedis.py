import redis
from file import data1
import logging
logging.getLogger().setLevel(logging.INFO)


class operateRedis():

    def __init__(self):
        self.__redis=redis.StrictRedis(host=data1.host,port=6379,password="")

    def set(self,key,value):

        self.__redis.set(key,value)
        logging.info("预制缓存数据 " + '"'+key+'"'+':' + '"' + value + '"' + " ---成功！！")

    def get(self,key):

        if self.__redis.exists(key):
            logging.info("查询缓存数据 " + '"' + key + '"' + " ---成功！！")
            return self.__redis.get(key)

        else:
            logging.info("未找到要获取的缓存数据key  " + '"' + key + '"' + "  ！！")
            return ""
    def remove(self,key):
        if self.__redis.exists(key):
            logging.info("删除缓存数据 " + '"' + key + '"' + " ---成功！！")
            return self.__redis.delete(key)

        else:
            logging.info("未找到要删除的缓存数据key  " + '"' + key + '"' + "  ！！")
            return ""

if __name__ == '__main__':
    r=operateRedis()
    r.set("gjc5","NJX5")
    # r.get("CCC")
    # r.remove("gjc2")
    # A = "aaaaaa"
    # B = str(r.get("zhy"))
    # print(A + B)





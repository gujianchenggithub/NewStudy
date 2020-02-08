from Redis import operateRedis
#11212!2111111111
r = operateRedis.operateRedis()
r.set("gjc61", "NJX6")
r.get("CCC")

# r.remove("p1")




# A = "aaaaaa"
# B = str(r.get("zhy"))
# print(A + B)




# import logging
# logging.getLogger().setLevel(logging.INFO)
#
#
#
# logging.info('这是 loggging info message')








# #coding=utf-8
# #连接数据库测试
# import  pymysql
# #打开数据库
# db = pymysql.connect(host="localhost",user="root",password="root",db="test")
# #使用cursor()方法获取操作游标
# cur = db.cursor()
# #查询操作
# sql = "select * from books"
# try:
#     # 执行sql语句
#     cur.execute(sql)
#     results = cur.fetchall()
#     #遍历结果
#     for rows in results:
#         id = rows[0]
#         name = rows[1]
#         price = rows[2]
#         bookcount = rows[3]
#         author = rows[4]
#         print("id: {}, name: {}, price: {}, bookcount: {}, author: {}".format(id,name,price,bookcount,author))
# except Exception as e:
#     raise e
# finally:
#     db.close()
# ————————————————
# 版权声明：本文为CSDN博主「崔昕阳」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Cuixinyang19_/article/details/80060294
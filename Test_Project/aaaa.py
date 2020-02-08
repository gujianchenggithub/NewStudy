import pymysql


conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='',  # password也可以
                       db='empirecms',
                       charset='utf8')  # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("select * from phome_ecms_article where title='历史上的父子宰相'")

# 4. 获取查询结果
result = cur.fetchone()
print(result)
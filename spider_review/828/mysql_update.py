import pymysql

# 更新数据

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

# 2.创建游标
cursor = db.cursor()

# .写sql语句
sql = 'update students set age = %s where name = %s'
try:
    # 执行sql 语句
    cursor.exrcute(sql, (25, 'berg'))
except:
    db.rollback()
db.close()

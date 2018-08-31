import pymysql

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

# 2.创建光标
cursor = db.cursor()

# 3.写sql语句
sql = 'delete from students where age < 20 '
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

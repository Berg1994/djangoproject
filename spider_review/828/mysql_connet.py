import pymysql

# 配置数据库参数
db = pymysql.connect(host='localhost', port=3306, password='123456', charset='utf8', user='root')
# 创建游标
cursor = db.cursor()
# 执行sql语句
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('create database spiders default character set utf8')
db.close()

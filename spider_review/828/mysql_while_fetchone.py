import pymysql

#1.配置数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='spider_828')

#2.创建光标
cursor = db.cursor()

#.sql语句

sql = 'select * from students where age >= 20'
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')


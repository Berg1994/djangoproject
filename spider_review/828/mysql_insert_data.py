import pymysql

id = '2012001'
user = 'berg'
age = 20
#1.配置数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='spider_828')
#2.创建游标
cursor = db.cursor()
#3.写sql语句
sql = 'insert into students(id,name,age) values(%s,%s,%s)'

#4.执行sql语句 因为要写入数据库 我们需要用try 并回滚
try:
    cursor.execute(sql,(id,user,age))
    #提交数据
    db.commit()
except:
    db.rollback()
#关闭数据库
db.close()

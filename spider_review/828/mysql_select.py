import pymysql

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

#2.创建光标

cursor = db.cursor()

#3.写sql语句

sql = 'select * from students where age >= 20'

try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    #fetchone方法导致指针往下偏移1位 所有以后查找所有时只剩1位 总共应该是2位
    results = cursor.fetchall()
    print('Result:',results)
    print('Result Type:',type(results))
    for row in results:
        print(row)
except:
    print('Error')
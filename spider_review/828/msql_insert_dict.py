import pymysql

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')
# 2.创建光标
cursor = db.cursor()
# 3.写sql语言
data = {
    'name': 'berg',
    'age': 16,
    'id': '20120001'
}

table = 'students'

keys = ','.join(data.keys())

values = ','.join(['%s'] * len(data))

sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

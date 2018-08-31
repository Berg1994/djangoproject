import pymysql

data = {
    'name': 'berg',
    'age': 16,
    'id': '123455',

}

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

# 2.创建光标
cursor = db.cursor()

# 3.写sql语句
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data.values()))

sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)

# 4.执行sql
try:
    if cursor.execute(sql, tuple(data.values())): #name,age,id
        print('插入完成')
        db.commit()
except:
    db.rollback()
    print('插入失败')
db.close()
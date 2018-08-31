import pymysql

# 1.配置数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

# 2.创建光标
cursor = db.cursor()

# 3.写sql 语句
data = {
    'id': '2019001',
    'name': 'bob',
    'age': 22
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data.values()))

sql = 'insert into {table}({keys}) values({values}) on duplicate key update'.format(table=table, keys=keys,
                                                                                    values=values)

update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update

try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('successful')
        db.commit()
except:
    db.rollback()
    print('failed')


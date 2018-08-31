import pymysql
#1.配置数据库信息
db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='spider_828')

#2.创建游标
cursor = db.cursor()

#3.写sql语句
sql = 'create table if not exists students (' \
      'id varchar(255) not null,' \
      'name varchar(255) not null, ' \
      'age int not null,' \
      'primary key (id)) '

#4.用光标执行sql语句
cursor.execute(sql)

#5.关闭数据库
db.close()

import csv

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'mike', 20])
    writer.writerow(['10002', 'bob', 22])
    writer.writerow(['10003', 'jack', 24])

# 传入delimiter修改列与列之间的分隔符 y因为有中文所以需要编码
with open('data2.csv', 'w', encoding='utf8') as e:
    writer = csv.writer(e, delimiter=' ')
    writer.writerow(['', '语文', '数学', '英语'])
    writer.writerow(['王大锤', '79', '60', '53'])
    writer.writerow(['李玉', '93', '94', '90'])
    writer.writerow(['箐显', '98', '67', '99'])

#同时多行写入 用writerows
with open('data3.csv','w') as r:
    writer = csv.writer(r)
    writer.writerows([['id','name','age'],[1,'berg',20],[2,'nana',22],[3,'tom',23]])

#写入字典
with open('data4.csv','w') as d:
    key_names = ['id','name','age']
    writer = csv.DictWriter(d,fieldnames=key_names)
    writer.writeheader()
    writer.writerow({'id':1001,'name':'berg1','age':22})
    writer.writerow({'id':1002,'name':'berg2','age':23})
    writer.writerow({'id':1003,'name':'berg3','age':24})


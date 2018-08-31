import pymongo

# 1.配置客户端数据库
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
db = client['test']

# 3.指定集合（表）
collection = db['students']

# 4.插入数据
student1 = {
    'id': '20170102',
    'name': 'berg',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170103',
    'name': '野菊',
    'age': 24,
    'gender': 'male'
}

result = collection.insert([student1, student2])
print(result)

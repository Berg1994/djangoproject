import pymongo

# 1.客户端数据库配置
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
# db = client.test
db = client['test']

# 3.指定集合（表）
# collection = db.students
collection = db['students']

# 插入数据
student = {
    'id': 20170101,
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert(student)
print(result)

import pymongo

# 1.配置客户端数据库

client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
db = client['test']

# 3.指定集合（表）

collection = db['students']

# 4.更新数据
condition = {'name': 'berg'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)

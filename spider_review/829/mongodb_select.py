import pymongo

# 1.配置客户端数据库
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
db = client['test']

# 3.指定集合
collection = db['students']

# 4.查询集合
result = collection.find_one({'name': 'berg'})
# print(type(result))
# print(result)
# 生成器
result2 = collection.find({'gender': 'male'})
for res in result2:
    # print(res)
    pass
# print(type(result2))
#查询年龄大于20岁的
result3 = collection.find({'age': {'$gt': 20}})
print(result3)
for res in result3:
    print(res)


#计数
result4 = collection.find().count()
print(result4)

#排序
result5 = collection.find().sort('name',pymongo.ASCENDING)
for res in result5:
    print(res['name'])
    

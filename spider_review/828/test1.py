data = {
    'name': 'berg',
    'age': 15,
    'id': '111101'
}

data1 = data.keys()
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
keys2 = ','.join(data)

print(keys,values,data1,keys2)
print(data)
print(data.keys())
print(type(data.keys()))
print(' '.join(data.keys()))
print(type(keys))
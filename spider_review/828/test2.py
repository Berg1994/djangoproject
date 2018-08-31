data = {
    'name': 'berg',
    'age': 15,
    'id': 11112
}

sql = 'insert into {table}({keys}) values({values}) on duplicate key update'.format(table=1,keys=2,values=3)

update = ','.join(" {key} = %s".format(key=key) for key in data)

sql += update

print(sql)

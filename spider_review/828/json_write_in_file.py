from json import dumps

data = [{
    'name': '王伟',
    'age': 18,
    'gender': 'man',
    'birthday': '1990-12-21'
}]
#因为有中文 不适用encoding编码就会出现乱码  下面不用ensure_ascii 就会是unicode
with open(data[0]['name'] + ".txt", 'w', encoding='utf8') as f:
    f.write(dumps(data, ensure_ascii=False))

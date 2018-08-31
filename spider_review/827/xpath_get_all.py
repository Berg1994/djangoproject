from lxml import etree

html = etree.parse('./text.html',etree.HTMLParser())
print(html)
print(type(html))
result = etree.tostring(html)
print(result)

res = html.xpath('//*')
print(res)
print(type(res))
print(res[0])
print(type(res[0]))
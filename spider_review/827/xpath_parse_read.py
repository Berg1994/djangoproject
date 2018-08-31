from lxml import etree

html = etree.parse('./text.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf8'))
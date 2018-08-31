from lxml import etree
#etree对象 元素树
html = etree.parse('./text.html',etree.HTMLParser())
# print(html)
#获取父元素
get_parent_node = html.xpath('//a[@href="link4.html"]/../@class')
print(get_parent_node)

#法2
get_parent_node2 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(get_parent_node2)
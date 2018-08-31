from lxml import etree

text = """

<li class="li li-first"><a href="link.html">first item</a></li>
"""

html = etree.HTML(text)
result = html.xpath('//li[@class="li li-first"]/a/text()')
result1 = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)
print(result1)

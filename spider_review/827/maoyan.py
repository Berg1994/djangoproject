import json
import re
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}


def get_one_page(url):
    """
    获取猫眼电影分类页面
    :param url: 猫眼电影链接
    :return: 返回响应
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('movies_into.txt', 'a', encoding='utf8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    """
    启动爬取
    """
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html.text)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

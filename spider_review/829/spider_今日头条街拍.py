import json
import os
import re
from multiprocessing.pool import Pool
from time import sleep

import requests
from urllib.parse import urlencode
import jsonpath


# 获取接口响应
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'form': 'gallery'
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return get_all_html_urls(response.json())
    except requests.ConnectionError:
        return None


# 获取接口链接
def get_all_html_urls(text):
    """
    分析接口json数据 提起所有页面链接
    :param text: 接口文档
    :return: 所有链接
    """
    # print(text)
    try:
        all_html_urls = jsonpath.jsonpath(text, "$..share_url")
        return get_html_images(all_html_urls)
    except Exception as e:
        print(e)
        pass


def get_image_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    # 获取响应
    response = requests.get(url=url, headers=headers)
    # 通过正则匹配获取接口内容
    try:
        get_url_text = re.findall('gallery: JSON.parse\\(\\"(.*)\\"\\)', response.text)[0]
    except Exception as e:
        print(e)
        return None
    # 通过替换清洗数据
    get_url_string_type_text = get_url_text.replace('\\', '')
    # 通过loads方法把字符串转换成字典
    get_dict_type_text = json.loads(get_url_string_type_text)
    # 通过jsonpath 方法获取值
    images_url = jsonpath.jsonpath(get_dict_type_text, "$..url")
    return get_images(images_url)


def get_html_images(urls):
    for url in urls:
        image_urls = get_image_html(url)
        get_images(image_urls)


def get_images(image_list):
    cut_list = {}
    if image_list:
        for image in image_list:
            if (image.split('/')[-1]) not in cut_list:
                cut_list[(image.split('/')[-1])] = 1
                # print(image)
                # print((image.split('/')[-1]))
                if not os.path.exists('./街拍'):
                    os.mkdir('./街拍')
                try:
                    filename = image.split('/')[-1] + '.jpg'
                    path = '街拍/' + image.split('/')[-1] + '.jpg'
                    response = requests.get(image)
                    if response.status_code == 200:
                        img = response.content
                        with open(path, 'wb') as f:
                            print('正在下载', filename + '。。。。。。。')
                            f.write(img)
                            sleep(3)
                            print(filename, '下载完成。。。。。。。')
                    else:
                        print('Already Downloaded', filename)
                except requests.ConnectionError:
                    print('Failed to save Image')


def main(offset):
    # for page in range(2, 20):
        # offset = page * 20
        print('-----正在爬取 第 %s 页------' % (offset // 20), '获取第%s 到 第%s 资源' % (offset - 20, offset))
        get_page(offset)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END)])
    pool.map(main, groups)
    pool.close()
    pool.join()

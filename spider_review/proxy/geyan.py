import re
import urllib.request
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}


def parse_html(response, charsets=('utf8','gb2312')):

    for charset in charsets:
        try:
            res = response.decode(charset)
            print(res)
            return res
        except Exception as e:
            pass



def get_urls(html):
    # print(html)
    url = re.findall(r'<<a href="(.+)" title=.+? target="_blank">.+?</a>', html)
    print(url)
    if url:
        return url

def get_html(url):
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    main_html = parse_html(response)
    html_urls = get_urls(main_html)


def main():
    url = 'http://www.geyan123.com/'
    get_html(url)


if __name__ == '__main__':
    main()

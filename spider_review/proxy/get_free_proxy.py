# 西祠代理爬取
import random
import time
import requests
import urllib.request
from bs4 import BeautifulSoup


# 通用方法
class CommanClass(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
        }
        self.testurl = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

    # 获取响应
    def get_response(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        resp = urllib.request.urlopen(req, timeout=3)
        content = resp.read()
        return content

    def is_alive(self, proxy):
        try:
            resp = 0
            for i in range(3):
                # 通过handler 和opener 发送请求 查看响应状态码

                # 访问
                try:
                    resp = requests.get(url=self.testurl, proxies={'http': proxy}, timeout=3)

                except Exception as e:
                    print('响应错误')
                    return False
            if resp.status_code == 200:
                print('IP %s 可以使用' % proxy)
                return True
        except Exception as e:
            return False


# 代理池
class ProxyPool(object):
    def __init__(self, proxy_finder):
        self.pool = []
        self.proxy_finder = proxy_finder
        self.cominstan = CommanClass()

    def get_proxies(self):
        self.pool = self.proxy_finder.find()
        for pl in self.pool:
            if self.cominstan.is_alive(pl):
                # print('IP %s 可以使用 正在存入文本' % pl)
                continue
            else:
                # print('IP %s 无法使用 已删除' % pl )
                self.pool.remove(pl)

    def get_one_proxy(self):
        return random.choice(self.pool)

    def writeToTxt(self, file_path):
        try:
            with open(file_path, 'w+') as f:
                for item in self.pool:
                    f.write(str(item) + '\n')
        except IOError:
            print('fail to open file')


# 定义基类
class IProxyFinder(object):
    # 初始化属性 获取pool列表
    def __init__(self):
        self.pool = []

    # 构建方法    
    def find(self):
        return


class XiciProxyFinder(IProxyFinder):
    def __init__(self, url):
        # m单继承默认可以不写 super不是父类，而是继承顺序的下一个类
        super(XiciProxyFinder, self).__init__()
        # super().__init__()
        self.url = url
        self.cominstan = CommanClass()

    def find(self):
        for i in range(1, 2):
            # 页码规则 爬取20页 方法源于通用类
            content = self.cominstan.get_response(self.url + str(i))
            # 创建bs实例
            soup = BeautifulSoup(content, 'lxml')
            # 获取所有ip 内容
            ips = soup.findAll('tr')
            for x in range(2, len(ips)):
                # 循环取出每个Ip
                ip = ips[x]
                tds = ip.findAll('td')
                if tds == []:
                    continue
                # 拼接ip 和端口
                ip_temp = tds[1].contents[0] + ':' + tds[2].contents[0]
                # 添加到代理池
                self.pool.append(ip_temp)
        time.sleep(1)
        return self.pool


if __name__ == '__main__':
    finder = XiciProxyFinder("http://www.xicidaili.com/nn/")
    ppool_instance = ProxyPool(finder)
    ppool_instance.get_proxies()
    ppool_instance.writeToTxt("proxy.txt")

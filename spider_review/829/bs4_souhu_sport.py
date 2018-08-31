from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


# 获取首页内容
def get_html_text(url):
    response = requests.get(url, headers=headers)
    # print(response.text)
    text = response.text.encode('gbk', 'ignore').decode('gbk')
    return text

#获取页面链接
def get_html_urls(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    news_tag_list = soup.select('.f14list a')
    news_urls_list = [url.attrs['href'] for url in news_tag_list]
    return news_urls_list

#获取新闻内容
def get_news_html(urls):
    for news_url in urls:
        news_text = ''
        res_text = requests.get(news_url, headers=headers).text
        soup = BeautifulSoup(res_text,'lxml')
        news_content = soup.select('article p')
        #[print(text.get_text()) for text in soup.select('article p') if text.get_text()]
        title = news_content[0].get_text()
        for news in news_content[1:]:
            news_text += news.get_text()
        with open(title + '.txt', 'w',encoding='utf8') as f:
            f.write(title + '\n' + news_text)



def main():
    url = 'http://sports.sohu.com/s2018/2873/s544995337/'
    text = get_html_text(url=url)
    urls = get_html_urls(text)
    news_content = get_news_html(urls)


if __name__ == '__main__':
    main()

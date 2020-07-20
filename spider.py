from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame


def get_soup(url):
    '''
        获取bs对象
        通过request模块获取被爬取的url内容并且转换为一个bs对象,本方法只支持get请求，未做扩展。
        Args: 
            url: 被爬取的目标网站
        Return:
            返回被解析的bs对象
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    html = requests.get(url, headers, timeout=10)
    return BeautifulSoup(html.text)


def find_content(soup, res):
    '''
        筛选出内容
        从一个bs对象中筛选出需要爬取的内容，放入到指定的容器中
        Args:
            soup : 被筛选的bs对象
            res: 存放数据的目标容器
        Return :
            因为传入的是一个list（引用类型）所以不需要返回值
    '''
    table = soup.find('table')
    content_list = table.find_all('tr')
    for item in content_list:
        td = item('td')
        if(not bool(td)):
            continue
        item_content = []
        for item in td:
            item_content.append(item.text)
        res.append(item_content)


base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
# 爬取多页数据
res = []
for i in range(10):
    url = base_url + str(i+1) + '.shtml'
    find_content(get_soup(url), res)
df = DataFrame(res, columns=['投诉编号', '投诉编号', '投诉车系',
                             '投诉车型', '问题描述', '典型问题', '投诉事件', '投诉状态'])
df.to_excel('./cart_complaint.xlsx')

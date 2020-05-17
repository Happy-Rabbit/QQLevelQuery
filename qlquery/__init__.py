# coding: utf-8

from my_fake_useragent import UserAgent as ua
from requests import Session
from bs4 import BeautifulSoup as BS
import time

__author__ = "Happy Rabbit"
__author_email__ = "happy.rabbit.yy@outlook.com"

__all__ = ['__author__', '__author_email__', '__all__', 'bs', 'log', 'QueryQQ', 'Query']

bs = lambda x: BS(x.content, "html.parser")
log = lambda x='', logLevel='INFO', y='QueryQQLevel': print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}{str(time.time()-int(time.time()))[1:4]} {y}] {logLevel} {x}', flush=True)

class QueryQQ():
    def __init__(self, qq: int = 0, retry: int = 3, proxies: dict = {}, isDebug: bool = True) -> None:
        """参数设置:

qq:         int     需要查询的QQ账号        默认为 0

retry:      int     查询失败的重试次数      默认为 3

proxies:    dict    请求的代理服务器        默认为 {}

isDebug:    bool    是否显示调试信息        默认为 True"""
        self.qq = qq
        self.retry = retry
        self.session = Session()
        self.session.proxies = proxies
        self.session.headers['User-Agent'] = ua().random()
        self.targetUrl = "http://www.175hd.com/level/{qq}.html"
        self.isDebug = isDebug

    def query(self, qq: int = None) -> int:
        """参数设置:

qq:         int     需要查询的QQ账号        默认为 0"""
        try:
            if qq:
                self.qq = qq
                log(f"账号已改为 {qq}") if self.isDebug else None
            log("请求中...") if self.isDebug else None
            request = self.session.get(self.targetUrl.format(qq=self.qq))
            log("请求成功") if self.isDebug else None
            targetBS = bs(request) if request.status_code == 200 else None
            if not targetBS:
                raise ValueError("the status code of the request is not 200 OK.")
            tdList = targetBS.find_all('td')
            targetInfo = [i.text.strip() for i in tdList if b'\xe7\xba\xa7'.decode('utf-8') in i.text.strip()][1]
            log("已找到QQ等级") if self.isDebug else None
            return int(targetInfo[:-1])
        except Exception as e:
            log(e.__repr__(), 'WARN')
            if self.retry > 0:
                self.retry -= 1
                return self.query()
            else:
                return None
    
    def config(self, qq = None, retry = None, proxies = None, isDebug = None):
        """参数设置:

qq:         int     需要查询的QQ账号        为 None 表示不更改(默认)

retry:      int     查询失败的重试次数      为 None 表示不更改(默认)

proxies:    dict    请求的代理服务器        为 None 表示不更改(默认)

isDebug:    bool    是否显示调试信息        为 None 表示不更改(默认)"""
        if qq:
            self.qq = qq
        if retry:
            self.retry = retry
        if proxies:
            self.proxies = proxies
        if isDebug:
            self.isDebug = isDebug

Query = QueryQQ
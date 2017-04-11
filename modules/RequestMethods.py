#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, lxml.html

def FollowingCollect(url, re=None,HTTP_PROXY=None, HTTPS_PROXY=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

    # Proxy Address
    proxies = {
        "http": HTTP_PROXY,
        "https": HTTPS_PROXY,
    }

    session = requests.Session()

    # Cookie
    cookie = {
        'Cookie': 'You Cookie'
        }
    source = session.get(url, headers=header, cookies=cookie, proxies=proxies).content

    if re:
        selecter = lxml.html.fromstring(source)

        infoList = selecter.xpath(re)

        return infoList

    return source

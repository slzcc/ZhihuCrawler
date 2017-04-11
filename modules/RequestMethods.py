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
        'Cookie': 'q_c1=6ea1b7ab7de948a98a3af6ae84c9f784|1491573404000|1491573404000; d_c0="AFDC11_ckguPTnv5g1-2QedSBkuvqORQd8M=|1491614224"; _zap=45d72be3-08a0-41c8-a7c4-0f6dc6516636; _xsrf=4d385f3ece969b2dd6ae5acb1d6589d6; capsion_ticket="2|1:0|10:1491805669|14:capsion_ticket|44:YzJlYzI2YmZmYzdjNGQ3YWFkY2E5YzAwYzk3Y2FjYmU=|1b0e99d9c7b226eb8f8198cf3281870e92dcec7bb856aa8cf979c953da0a8ef4"; cap_id="NjcxZjMyYjFkMTkzNDM4ZGI3MmZiMWY2NmUwYTI0MTQ=|1491805679|735db5e2c334ee5d0423d8341664a932ee393d8f"; l_cap_id="ZjNhYjNlYjhkZjQzNGE1M2FkOGEyMjVmMTMzMjEwMWE=|1491805679|4e33221dc0590f412a5696e6832318e84b454f7e"; aliyungf_tc=AQAAAPmdPk3Sfw4ABErKAewfEFiBG94Q; z_c0=Mi4wQUhEQ3M4dTJsUXNBVU1MWFg5eVNDeGNBQUFCaEFsVk5JdDBTV1FDYVloMnljQnBBTDJid3dRU1lFNDExUktMaG5R|1491868290|f2b757c6f6998456b3af41b21dcd22e90bf89e6e; __utma=51854390.1759389902.1491796454.1491831365.1491868292.5; __utmb=51854390.0.10.1491868292; __utmc=51854390; __utmz=51854390.1491796454.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20170410=1^3=entry_date=20170407=1'
        }
    source = session.get(url, headers=header, cookies=cookie, proxies=proxies).content

    if re:
        selecter = lxml.html.fromstring(source)

        infoList = selecter.xpath(re)

        return infoList

    return source
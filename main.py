#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import threading
import time
import math
import json
from modules.RequestMethods import FollowingCollect
from upload import Upload

HTTP_PROXY='http://42.58.220.107:59913'
HTTPS_PROXY='http://42.58.220.107:59913'

ElasticServer = '127.0.0.1:9200'
RedisServer = '127.0.0.1'

# 迭代次数
PeopleNum = 8


RedisServer_db_one = redis.StrictRedis(host=RedisServer, port=6379, db=10)
RedisServer_db_two = redis.StrictRedis(host=RedisServer, port=6379, db=11)

num = 1
Counters = 1

Read_list = []
Record_list = []
Temp = []
threads = []

def ListAdd(data):
    global Temp, num, Read_list
    followers_json = json.loads(data)
    for item in followers_json['data']:
        Temp.append(item['url_token'])
    Read_list = Temp
    num += 1

def Main(PeopleNum):
    global Read_list, Temp
    Temp = []
    if PeopleNum == 1:
        KeyNum = RedisServer_db_two.keys()
        for item in range(1, len(KeyNum)):
            ThreadNum = (math.ceil(len(KeyNum) / 100 + 1))
            global Counters, threads
            for i in range(0, ThreadNum):
                time.sleep(1.5)
                locks = threading.Lock()
                T = UploadThread(RedisServer_db_one, Counters, ElasticServer)
                T.start()
                Counters += 1
                threads.append(T)
            for t in threads:
                t.join()
        return 1
    for item in Read_list:
        T = TaskThread(item)
        T.start()
        threads.append(T)
    for t in threads:
        t.join()
    threads = []
    return PeopleNum * Main(PeopleNum - 1)


class TaskThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.Data = data

    def run(self):
        locks.acquire()
        global num, Temp, Record_list
        if self.Data not in Record_list:
            RedisServer_db_one.set(num, self.Data)
            Record_list.append(self.Data)
            print('RQ_User_Token: {}, Num: {}'.format(self.Data, num))
            JSON_Data_Url = 'https://www.zhihu.com/api/v4/members/{}/followees?include=data%5B*%5D.url_token&offset=0&per_page=30&limit=30'.format(self.Data)
            RedisServer_db_two.set(num, JSON_Data_Url)
            Url_list = FollowingCollect(JSON_Data_Url, HTTP_PROXY=HTTP_PROXY, HTTPS_PROXY=HTTPS_PROXY)
            ListAdd(Url_list)
        locks.release()

class UploadThread(threading.Thread):
    def __init__(self, redisServer, num, elasticServer):
        threading.Thread.__init__(self)
        self.RedisServer = redisServer
        self.Num = num
        self.ElasticServer = elasticServer

    def run(self):
        time.sleep(1)
        locks.acquire()
        Upload(self.RedisServer, self.Num, self.ElasticServer)
        locks.release()

if __name__ == '__main__':
    RQ_Urls = 'stone-cok'
    Read_list.append(RQ_Urls)
    locks = threading.Lock()
    Main(PeopleNum)
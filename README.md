# Python 爬取知乎用户信息
>使用说明: 

1)、内部使用了不少第三方模块请按照下面模块列表进行安装
```
$ pip install redis requests lxml elasticsearch
```
>如果模块没有也会报错，请跟进错误进行安装。

2)、在 `main.py` 文件里会附带 HTTP/HTTPS PROXY 变量，如果不需要请修改 `modules/RequestMethods.py` 文件的
```
source = session.get(url, headers=header, cookies=cookie, proxies=proxies).content
```
修改为：
```
source = session.get(url, headers=header, cookies=cookie).content
```
3)、这里需要用户提供知乎登入后的 Cookie ，请使用 Chorme 浏览器代码审查工具获取 Cookie 信息填写进入 `modules/RequestMethods.py` 的 cookie JSON 变量：
```
cookie = {'Cookie': 'You Cookie'}
```
4)、需要提供 Redis Server
默认使用本地环境，可直接使用 Docker 启动临时测试环境：
```
$ docker run -p 6379:6379 --name some-redis -d registry.aliyuncs.com/slzcc/redis
```
>可以更改 `main.py` 文件变量来变更自定义服务地址。
5)、需要提供 ElasticSearch Server 
默认使用本地环境，可直接使用 Docker 启动临时测试环境：
```
$ docker run -p 9200:9200 --name some-elasticsearch -d registry.aliyuncs.com/slzcc/elasticsearch
```
>如果 elasticsearch 未能正常启动求根据错误需求进行修改，通常是因为 vm 参数大小和文件句柄大小过小导致。
>以更改 `main.py` 文件变量来变更自定义服务地址。
6)、启动完成后请执行
```
$ python main.py &
```
>默认全部使用多线程工作，需要通过后台运行否则出现错误后无法退出终端。
>默认会迭代 8 次知乎用户的追随者列表，如果想迭代更多次请修改 `main.py` 文件的 `PeopleNum` 变量。
>注意：如果更改了 `PeopleNum` 变量的值很大，请确保您的机器可以支撑，多线程是对每一个被迭代后使用的追随者再去迭代，这里是深度搜索的所以开设的线程也会达到上万的级别。
7)、如果出现 502 等错误，有可能被 “知乎网” 屏蔽了 IP 地址，请更换代理进行尝试。

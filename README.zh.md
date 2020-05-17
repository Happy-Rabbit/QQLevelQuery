# QQLevelQuery (Python Package)

## 作者: Happy-Rabbit
## [联系我](mailto:happy.rabbit.yy@outlook.com?subject=关于QQLevelQuery模块的反馈&body=%0d%0d%0d%0d发送者:[你的名字]%0d联系方式:[联系方式])

[返回 README](./README.md)

[前往简介](#简介)

### 下一步的想法(初步):

- [ ] 用`aiohttp`重新开发一个异步的类
- [ ] 增加一些其他的功能(暂时还不知道加点啥2333)

### 版本:

最新:

#### v 1.0.0
- [x] 添加了基本的类 - `class QueryQQ()` 
- - 函数 `query()` 可以查询QQ等级(如果失败会返回 None)
- - 函数 `config()` 可以改变变量的值
- - 变量 `isDebug` 可以控制是否输出 INFO 日志
- [x] 另一个类 `Query` 指向的是 `QueryQQ` (设置的别名)

旧版:

暂无

### 简介:

这个模块可以用来查询QQ等级(基于网页 [*米粒QQ等级查询*](http://www.175hd.com/level/) 开发)

由于QQ机器人的发展, 导致线上营销人员大量出现, 越来越多的低等级营销bot会尝试申请加群并在群里发送广告信息.

这个模块可以帮助管理员查询QQ的等级来筛选加群申请.

***!!! 注意 !!!***

**如果一天内查询信息过多, 可能导致模块无法正常工作(比如IP地址被查询服务器封禁). 甚至可能需要承担法律后果!!!**

### 使用方法:

打开cmd/Terminal, 用 `cd` 命令到本文件夹.

运行 `python(3) setup.py build` 和 `python(3) setup.py install` 来安装本模块.

**注: 需要的包如下:**
| 包名称 | pip的安装包名称 | 版本 |
| :---: | :---: | :---: |
| beautiful soup 4 | beautifulsoup4 | 4.6.0 |
| my fake useragent | my-fake-useragent | 0.1.6 |
| requests | requests | 2.23.0 |

**如果本模块无法正常运行, 请尝试重新手动安装上述模块**

运行 Python (Python 版本必须高于 3.5)

```python
>>> # 这只是个例子
>>> import qlquery
>>> query = qlquery.Query(qq=xxxx, isDebug=False) # 或者使用 qlquery.QueryQQ()
>>> # 运行 print(query.__doc__) 来查看帮助信息
>>> query.query(qq=xxxxxxx)
64
>>> query.config(qq=xxxx, retry=xxx, proxies=xxx, isDebug=True/False)
>>> query.query()
35
>>> query.config(isDebug=True)
>>> query.query()
[2020-05-17 22:05:26.78 QueryQQLevel] INFO 当前请求的QQ账号为: xxxx
[2020-05-17 22:05:26.78 QueryQQLevel] INFO 当前请求的代理为: 空
[2020-05-17 22:05:26.78 QueryQQLevel] INFO 请求中...
[2020-05-17 22:05:28.15 QueryQQLevel] INFO 请求成功
[2020-05-17 22:05:28.17 QueryQQLevel] INFO 已找到QQ等级
35
```
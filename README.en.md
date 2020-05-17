# QQLevelQuery (Python Package)

## author: Happy-Rabbit
## [contact me](mailto:happy.rabbit.yy@outlook.com?subject=about%20the%20QQLevelQuery%20module&body=%0d%0d%0d%0dSender:[Your_Name]%0dContact:[Contact])

[Return README](./README.md)

[Go to Description](#Description)

### What's Next... (just an idear)

- [ ] Rewrite a class used `aiohttp`
- [ ] Maybe can add another function...

### Versions:

newest:

#### v 1.0.0
- [x] Added the Based class - `class QueryQQ()` 
- - function `query()` can query the QQ level(if failed, return None)
- - function `config()` can modify the variables.
- - variable `isDebug` can control the function whether print the INFO logs.
- [x] Another class named `Query` is alias to `QueryQQ`

old:

None

### Description:

This module can query the QQ Level (based on the website [*米粒QQ等级查询*](http://www.175hd.com/level/))

Because of the development of QQ Bot, the advertiser and the online saleman become more and more. So, sometimes it may have some low-level accounts will try to join groups and send the advertisements in group.

This module can query the QQ level, to help the administrators to manager the group-add requests.

***!!! CAUTIONS !!!***

**If query the QQ accounts so many times in a day that can cause this module crashed(such as IP blocked and so on). Even cause legal liability!!!**

### Usage:

Start cmd/Terminal, then use command `cd` to this folder.

run `python(3) setup.py build` and `python(3) setup.py install` to install this module.

**Note: Used packages are:**
| Name | Package Name | Version |
| :---: | :---: | :---: |
| beautiful soup 4 | beautifulsoup4 | 4.6.0 |
| my fake useragent | my-fake-useragent | 0.1.6 |
| requests | requests | 2.23.0 |

**If the module cannot work normally, please try to reinstall packages**

Start the python (version should higher than 3.5)

```python
>>> # JUST A SAMPLE
>>> import qlquery
>>> query = qlquery.Query(qq=xxxx, isDebug=False) # or qlquery.QueryQQ()
>>> # Run print(query.__doc__) to view the help info
>>> query.query(qq=xxxxxxx)
64
>>> query.config(qq=xxxx, retry=xxx, proxies=xxx, isDebug=True/False)
>>> query.query()
35
>>> query.config(isDebug=True)
>>> query.query()
[2020-05-17 22:05:26.78 QueryQQLevel] INFO 请求中...
[2020-05-17 22:05:28.15 QueryQQLevel] INFO 请求成功
[2020-05-17 22:05:28.17 QueryQQLevel] INFO 已找到QQ等级
35
```
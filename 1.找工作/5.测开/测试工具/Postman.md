## 第一天
## 一、灵魂三问：

1. 什么是接口？

电脑：USB， 投影仪（数据传输）
软件：统称API（application programmer interface）。如微信提现和充值，支付宝支付接口，银联的支付接口（鉴权码：token, key, appkey）
接口包括：内部接口和外部接口
内部接口：开发人员自己开发的对自身系统提供的接口
外部接口：开发系统调用外部的，微信，支付宝，其他的接口
总结：接口软件就是提供给外部的一种服务，用于数据传输。

2. 软件为什么需要接口？

因为接口能够让内部的数据被外部进行修改。

3. 为什么要做接口测试？

（1）现在很多系统都是前后端分离，开发的进度不一样，需要把一开始开发出来的接口进行测试。
mock（模拟接口）
（2）基于安全的考虑，前端有验证很容易绕过，直接请求接口，特别：：身份证信息，银行卡，金钱交易。
（3）测试推崇的是测试左移，测试尽早的介入。

接口的本质：函数、方法、动作
接口测试的本质：测试接口能否正常的交互数据，权限控制以及异常场景的提示等。

## 二、接口返回的数据格式和json详解

1. json格式：三组数据 80%

{error_code:0, msg:"提现成功"， data: [] }
error_code:错误码，0代表成功，code
msg: 对错误码的中文说明
data:真正的返回的数据

   1. json就是一种数据类型，整型，小数，字符串
   2. json由两组数据组成(www.bejson.com 可以进行json格式的校验、编码加密)
      1. map对象，键值对，{key: value, key2:value2}
      2. 数组：[value1, value2, ...]

2. html格式

<html>
<title><title/>
<body>
<error_code>0<error_code/>
...
<body/>
</html>

3. xml格式

<?xml?version="1.0" encoding="utf-8">
<error_code>0</error_code>
...
</xml>


## 三、接口测试协议

1. webservice协议：接口地址：http://.......?wsdl

http://192.168.12.1:8080/addUser
http://192.168.12.1:8080/delUser
http://192.168.12.1:8080/putUser
http://192.168.12.1:8080/selUser
soap协议，wsdl
restful规则：
get获取数据
post提交数据
put修改数据
delete删除数据
http://192.168.12.1:8080/User (restful规则地址一样)

2. dubbo协议：接口地址dubbo://...

长连接、异步、适用于少量数据的传输，**大并发**

3. http协议：http://  80%

https = http + ssl安全传输协议 端口443
http 80
什么是http协议：超文本协议，主要用于浏览器和服务器之间交互数据，交互有两个部分：
请求：get post put delete
响应：1xx 响应信息 2xx 成功 3xx 重定向（跳转不传值） 4xx客户端错误 5xx服务端错误
请求部分包括：

1. 请求行：请求方式get,post,put,delete、请求地址、协议HTTP/1.1和HTTP/2...
2. 请求头：

accept:客户端可以接受的数据格式
x-requested-with:异步请求（异步请求是指在发送请求后，客户端不需要等待服务器返回响应就可以继续执行其他操作。相反，同步请求是指客户端发送请求后，必须等待服务器返回响应后才能继续执行其他操作。）
user-agent:客户端的用户，指定发送请求的用户代理（浏览器、应用程序等）
host:请求的主机的ip地址
accept-encoding接受的编码方式
connection:keep-alive：保持活跃、长连接
cookie:请求cookie信息（当客户端发送请求时，可以在请求头中添加**Cookie**字段，以将之前服务器发送给客户端的Cookie信息带回服务器。）
content-length:内容的长度
...

3. 空一行
4. 请求正文：

响应的部分：

1. 响应行：协议、响应码、响应信息

http/1.1 200 ok

2. 响应头：

sever:服务器
date:日期
content-type:text/html charset=utf-8
connection:keep-alive
x-powered-by:
set-cookie:响应cookie信息（服务器在响应中可以通过**Set-Cookie**字段将Cookie信息发送给客户端。客户端在接收到响应后，会将这些Cookie信息保存在本地，并在后续的请求中自动将这些Cookie信息添加到请求头中的**Cookie**字段中发送给服务器。）
content-length:

3. 空一行：
4. 响应正文：

## 四、企业接口测试的流程和方案？

1. 拿到api接口文档，熟悉接口的业务，接口地址、鉴权、入参数、出参数、错误码
2. 接口计划和方案

思路：
正例：输入正常的入参，查看接口是否返回成功
反例：
鉴权反例：为空，鉴权码错误、鉴权码已过期
参数反例：参数为空、类型异常、长度异常、
错误码的覆盖。
其他的场景：分页异常

3. 编写用例和评审
4. 执行接口测试
5. 输出接口测试报告

## 五、接口测试工具以及postman介绍
接口测试工具：
postman, jmeter, soupui, apipost, 抓包（fidder, charles）
postmax实践：见[https://www.bilibili.com/video/BV11K4y1J7sh?p=26&vd_source=afc0b67a7b6a49641c92c82a78e417a7](https://www.bilibili.com/video/BV11K4y1J7sh?p=26&vd_source=afc0b67a7b6a49641c92c82a78e417a7) P26 P27 (get post请求 + 每个按钮都是干什么的)

**add request请求的各个标签都是干什么的：**
Params:用于在get请求传参数
Authorization: Postmax自带的鉴权功能
headers:请求头
body：post请求参数
none:没有参数
form-data:既有文件又有键值对
x-www-from:只能传键值对
raw:json/txt/xml/html/js
binary:二进制
pre-request-script:接口请求之前的脚本。js 用来自动化验证响应的正确性
tests：断言代码
cookies:postman的cookie管理器
code:生成接口自动化脚本
--- 
**响应部分的页签**
body: 返回的数据
pretty:以json格式展示
raw:以文本形式展示
preview:以网页形式展示
cookie返回的cookie信息
headers响应头
testresults:断言结果

status:状态码
time:消耗时间
size:返回字节数

console: 控制台

-----2023.9.9晚

## 第二天
## 一、Postman内置动态参数（自带的不需要事先设置）

企业当中做接口测试的时候经常出现不能把参数写死
时间戳 ：{{$timestamp}}
生成0-1000的随机整数：{{$randomint}}
生成一个GUID的字符串：{{$guid}} 一个很长的字符串
## 

## 二、Postman环境变量和全局变量
开发环境、测试环境、预发布环境、线上环境

环境是全局变量：
环境中设置ip 为 api.weixin.ccom
url中更改为https://{{ip}}/...

不管是环境变量还是Globels都是全局变量。

## 三、接口关联(设置全局变量)

在断言中写代码来进行接口的关联

第一种提取方式：
获得token进行access_token变量不同requeset之间的关联
在1. 获得access_token接口中 tests断言中执行
```
//提取access_token的
var jsValue = JSON.parse(responseBody)
console.log(jsValue.access_token)
//把提取的值保存到全局变量
pm.globals.set("access_token", jsValue.access_token);
```
第二种提取方式：使用正则表达式
```
//使用正则表达式提取
var flag_id = responseBody.match(new RegExp('"id":(.+?),'))[1]
console.log(flag_id)

pm.globals.set("access_token", flag_id);
```

第三种提取方式：cookie
```
//cookie提取题, 从响应消息中的set-cookie中提取token
var csrf_token = postman.getResponseCookie('csrf_token').value;

pm.globals.set("csrf_token", csrf_token);
```

## 四、断言
//八种断言方式，八大元素定位

1. **断言返回码为200 一般用于状态断言**

pm.test("status code is 200", function(){
pm.response.to.have.status(200);
});

**一般状态断言不放在用例断言中，而是放在全局断言中，在collections中点击编辑可以看到**

2. **断言返回的结果中包括一个指定的字符串 用于业务断言**

pm.test("Body matchs string", function(){
pm.expect(pm.response.text().to.include("string_you_want_to_search"));
});

如果想要**_精确断言：_**
判断时间戳为例，不能直接用{{}}在断言中获得全局变量进行判断，要这样：
1、先在pre-request-script中获得时间戳并将时间戳设置为环境的全局变量(加前置脚本)
var times = Date.now()
pm.globals.set("times", times)
2、在断言中获取全局变量进行与消息体中的时间戳进行比较，但不能能{{}}获得全局变量，如下：
pm.test("Body matchs string", function(){
pm.expect(pm.response.text().to.include("string_you_want_to_search" + pm.globals.get("times")));
});

3. **对返回的结果做json字段检查  用于业务断言**

pm.test("your test name", function(){
var jsonData = pm.response.json();
pm.expect(jsonData.tags[0].id).to.eql(2);
});

4. **断言返回的结果等于一个字符串 用于业务断言**

pm.test("Body is correct", function(){
pm.response.to.have.body("response_body_string");
});

5. 断言响应头中包含指定的响应头

pm.test("Context-Type is present", function(){
pm.response.to.have.header("Content_Type");
});

6. **断言接口请求的时间小于200ms   用于性能断言**

pm.test("Response time is less than 200ms", function(){
pm.expect(pm.response.responseTime).to.be.below(200);
});

7. 断言一个post请求的返回的状态码是否在指定的范围里面

pm.test("Successful POST request", function(){
pm.expect(pm.response.code).to.be.oneOf([201, 202]);
});

8. 断言返回的状态码信息中包含指定的字符串

pm.test("Status code name has string", function(){
pm.response.to.have.status("ok");
});

## 第三天
## Postman接口测试项目实战
论坛项目为例：
项目中有哪些接口呢？除了登陆和注册之外，每个功能的实现都涉及到了接口

目的：通过调用postman自动实现登陆、自动实现评论、自动实现....

1. 抓包，形成用例文档
2. 用postman设计用例
3. newman实现非GUI自动化（得先安装node.js,然后再安装newman）
4. jenkins自动自动化


## 总结：

1. postman 用于接口测试 

以测试http接口为例，用postman来进行接口测试就是给指定的url和方法传递指定的参数，判断返回结果是否正确

对于一个collection的多个测试用例，实现用例的串行以实现自动化（后一个用例的参数可能会用到前一个用例的消息体中的内容），会用到断言提取消息体中的字段（会用到正则表达式），并设置全局变量，在paras或着body中用{{}}来引用全局变量/环境变量，以实现自动化，不用每个用例都手动设置，全部设置完成后，可以批量执行测试用例，自动测试一个业务流程。

在用例执行前需要执行脚本：就在pre-request script中写js脚本
在用例执行后对结果进行处理就用到了断言：tests中写脚本

还可以设置请求头

2. newman 

可以将 postman的collection中的用例集合导出，同时导出环境变量、全局变量

通过newman以非图形化界面的方式批量执行测试用例

3. jenkins

实习集成工具，可以导入任务，在指定的时间执行任务，这个任务可以是newman命令以完成自动化测试，并生成报告和结果，记录执行结果，还可以发邮件提醒












 






















 









# 阅读 MySQL必知必会 毕节

## 使用MySQL

1. 连接 mysql workbench(客户端软件)

    为了连接到MySQL，需要以下信息:

        - 主机名(计算机名)——如果连接到本地MySQL服务器，为localhost;
        - 端口(如果使用默认端口3306之外的端口);
        - 一个合法的用户名;
        - 用户口令(如果需要)。
  
    在连接之后，你就**可以访问你的登录名能够访问的任意数据库和表了。**

2. 选择数据库

`use crashcourse;`  -> Database changed

`show databases;` -> 现实当前用户下的所有数据库

`show tables;` -> 现实当前用户下的所有表

`show columns from customers;` 或 `describe customers;` -> 返回当前选择的数据库内可用表的列表

`SHOW STATUS;` -> 用于显示广泛的服务器状态信息;

`SHOW CREATE DATABASE;`和`SHOW CREATE TABLE;` -> 分别用来显示创
建特定数据库或表的MySQL语句;

`SHOW GRANTS;` -> 用来显示授予用户(所有用户或特定用户)的安
全权限;

`SHOW ERRORS;`和`SHOW WARNINGS;` -> 用来显示服务器错误或警告消息。

`help show;` -> 显示允许的SHOW语句。

## 检索数据

检索单个列

`select prod_name from products;`

检索多个列

`select prod_id, prod_name, prod_price from products;`

检索所有列

`select * from products;`

检索不同的行

DISTINCT关键字,此关键字指示MySQL **只返回不同的值。**（类似于集合操作）如果给出SELECT DISTINCT vend_id, prod_price，有两个列，distince会同时作用于两个列

`SELECT DISTINCT vend_id FROM products;`

限制结果

为了返回第一行或前几行，可使用**LIMIT子句**。

`select prod_name from products limit 5;` -> LIMIT 5指示MySQL返回 不多于5行

为得出下一个5行，可指定要检索的**开始行和行数**(limit 5,5) 

注意：**行0 检索出来的第一行为行0而不是行1。因此，LIMIT1,1 将检索出第二行而不是第一行。**

LIMIT 4 OFFSET 3意为从行3开始取4行，就像LIMIT 3, 4一样。

`select prod_name from products limit 5,5`

使用完全限定的表名

`select products.prod_name from products;`

`select products.prod_name from crashcourse.products;`

## 排序检索数据

排序数据

select为SQL语句， from为select语句的子句，有些子句是必须的，有些子句是可选的

排序子句ORDER BY(默认为升序)

`select prod_name from products ORDER BY prod_name;`

按多个列排序

首先按价格，然后再按名称排序。仅在多个行具有相同的prod_price 值时才对产品按prod_name进行排序。如果prod_price列中所有的值都是唯一的，则不会按prod_name排序。

```
select prod_id, prod_price, prod_name
from products
order by prod_price, prod_name
```

指定排序方向

默认的排序顺序**升序（ASC关键字 默认）（从A到Z）**，指定**降序关键字DESC**

```
select prod_id, prod_price, prod_name
from products
order by prod_price DESC
```

所有多个列，**DESC关键字只应用到直接位于其前面的列名**

```
select prod_id, prod_price, prod_name
from products
order by prod_price DESC, prod_name 
```
prod_price列以降序排序，而prod_name列(在每个价格内)仍然按标准 的升序排序。

注意：在字典(dictionary)排序顺序中，A被视为与a相同，这是MySQL (和大多数数据库管理系统)的默认行为。

使用ORDER BY和LIMIT的组合，能够找出一个列中最高或最低的值。

```
select prod_id, prod_price, prod_name
from products
order by prod_price DESC
limit 1
```
->price最高的值

## 6 过滤数据

- 使用WHERE子句

`select prod_name, prod_price from products where prod_price = 2.50;`

注意：WHERE子句的位置 在同时使用ORDERBY和WHERE子句时，应 该让**ORDER BY位于WHERE之后**

- where子句操作符

<img src='image.png' width='50%'>

- 检查单个值

`select prod_name, prod_price from products where prod_name = 'fuses';`

MySQL在**执行匹配时默认不区分大小写，所 以fuses与Fuses匹配。**

- 不匹配检查

`select vend_id, prod_name from products where vend_id <> 1003;`

**!=和<>都是可以的**

- 范围值检查

`select prod_name, prod_price from products where prod_price between  5 and 10;`

**注意写法：where prod_price between 5 and 10**

- 空值检查

在一个列不包含值时，称其为包含空值NULL。

使用WHERE子句IS NULL子句

`select prod_name from products where prod_price IS NULL`

注意：NULL与不匹配不是同一个东西

## 7 数据过滤

- 组合WHERE子句

操作符(operator) 用来联结或改变**WHERE子句中的子句**的关键 字。也称为逻辑操作符(logical operator)

**AND**操作符(用在WHERE子句中的关键字)

不止一个列进行过滤，多个条件

`select prod_name, prod_price, prod_name from products where vend_id = 1003 and prod_price <= 10;`

**OR**操作符

`select prod_name, prod_price, prod_name from products where vend_id = 1002 or vend_id = 1003;`

- 计算次序

WHERE可包含**任意数目的AND和OR操作符**。**允许两者结合**以进行复杂
和高级的过滤。

`where vend_id = 1002 or vend_id = 1002 and prod_price >= 10` SQL(像多数语言一样)在处理OR操作符前，**优先处理AND操 作符**。

使用 **括号()** 来改变计算次序 `(vend_id = 1002 or vend_id = 1002) and prod_price >= 10`

- IN操作符

与or操作符的作用一致

```
select prod_name, prod_price
from  products
where vend_id in (1002, 1003)
order by prod_name;
````

in相比or的优点：IN的最大优点是**可以包含其他SELECT语句**，使得能够更动态地建
立WHERE子句。

- NOT操作符

NOT操作符有且只有一个功能，那就是否定它之后所 跟的任何条件。

为了列出除1002和1003之外的所有供应
商制造的产品：

```
select prod_name, prod_price
from  products
where vend_id not in (1002, 1003)
order by prod_name;
```

not在与IN操作符联合 使用时，NOT使找出与条件列表不匹配的行非常简单。

## 8 用通配符进行过滤

- LIKE操作符

结合通配符完成复杂搜索

通配符：用来匹配值的一部分的特殊字符。

搜索模式(search pattern)： 由字面值、通配符或两者组合构
成的搜索条件。

通配符本身实际是SQL的WHERE子句中有特殊含义的字符

1. 百分号(%)通配符 : %表示任何字符出现 任意次数

e.g. 找出所有以词jet起头的产品

 `where prod_name LIKE 'jet%'` 
 
 **搜索结果区分大小写**，% 代表搜索模式中给定位置的**0个、1个或多个字符。**

 注意：
    1. 若词的尾部有空格，子句WHERE prod_name LIKE '%anvil'将不会匹配它们
    2. 注意NULL %不会匹配NULL


2. 下划线(_)通配符: 下划
线只匹配单个字符而不是多个字符。

`where prod_name LIKE '_ton anvil'`

## 9 用正则表达式 进行搜索

- 正则表达式介绍

正则表达式是用来匹配文本 的特殊的串(字符集合)， 

- 使用MySQL正则表达式

MySQL 用WHERE子句对正则表达式提供了初步的支持，允许你指定正则表达式， 过滤SELECT检索出的数据。（但可用的正则表达式仅为很小的部分）

1. 基本字符匹配

e.g. 检索列prod_name包含文本1000的所有行:

```
select prod_name
from products
where prod_name regexp '1000'
order by prod_name
```

它告诉MySQL:REGEXP后所跟的东西作 为正则表达式(与文字正文1000匹配的一个正则表达式)处理。

注意：

列值内进行匹配，如果被匹配的文本在 列值中出现，**列值中包括1000即可，不是全部，相当于 like '%1000%'**；如果想匹配整个列值，写法在后面；

`where prod_name regexp '.000'` **.是正则表达式语言中一个特殊的字符。它表示匹配任意一个字符**，因此，1000和2000都匹配 且返回。

2. 进行OR匹配

使用|

```
select prod_name
from products
where prod_name regexp '1000|2000'
```

表示列值中出现过‘1000’或者‘2000’行

3. 匹配几个字符之一

使用[], [123]表示当前位置匹配1或2或3

```
select prod_name
from products
where prod_name regexp '[123]Ton'
order by prod_name
```

正则表达式[123]Ton 为[1|2|3]Ton的缩写，也可以使用后者。

必须加[]，否则：1｜2｜3Ton就表示 出现1或2或3Ton 不是 1Ton或2Ton或3Ton的意思

注意：**字符集合也可以被否定**，[123] 匹配字符1、2或3，但[^123]匹配除这些字符外的任何东西。

4. 匹配范围

集合可用来定义要匹配的一个或多个字符，例[123456789] 为了简化

-> 可使用-来定义一个范围 即 [1-9] 或者 [a-z]匹配任意字母字符

5. 匹配特殊字符

正则表达式语言**由具有特定含义的特殊字符构成** ，如 .、[]、 |和-等。

但如果想匹配特殊字符

-> **为了匹配特殊字符，必须用\\为前导。\\-表示查找-，\\.表示查找.。** 即所谓的转义

注意：
1. 匹配\ 为了匹配反斜杠(\)字符本身，需要使用\\\。
2. 多数正则表达式实现使用单个反斜杠转义特殊字符，**但MySQL要求两个反斜杠**

<img src='image-1.png' width='50%'>

6. 匹配字符类

为更方便工作，可以使用预定义的字符集，称为字符类(character class)

<img src='image-2.png' width='50%'>

7. 匹配多个实例

表中的元字符在正则表达式中表示了特殊的意思

<img src='image-3.png' width='50%'>

8. 定位符

目前为止的所有例子都是匹配一个串中任意位置的文本。**为了匹配特定位置的文本，需要使用定位符。**

<img src='image-4.png' width='50%'>

`where prod_name regexp '^[0-9\\.]'`

表示 **.或任意数字**为串中**第一个字符时**才匹配它们

注意：1. ^的双重用途 ^有两种用法。在集合中(用[和]定义)，用它 来否定该集合，否则，用来指串的开始处。

## 10 创建计算字段

**拼接字段** 将值联结到一起构成单个值 （Concat()函数）

注意：多数DBMS使用+或||来实现拼接， MySQL则使用Concat()函数来实现

`select Concat(vend_name, '(', vend_country, ')') from vendors order by vend_name;`

结果：'Anvils R Us(USA)'

删除数据右侧多余的空格来整理数据，这可以 使用MySQL的RTrim()函数来完成(LTrim()(去掉串左边的空格)以及 Trim()(去掉串左右两边的空格)。)

`select Concat(RTrim(vend_name), '(', RTrim(vend_country), ')') from vendors order by vend_name;`

**使用别名**

`select Concat(RTrim(vend_name), '(', RTrim(vend_country), ')') as vend_title from vendors order by vend_name;`

**执行算术运算**

`select prod_id, quantity, item_price, quantity*item_price as expanded_price from orderitems where order_num = 20005`

![](image-5.png)

注意：SELECT 3*2;将返回6，SELECT Trim('abc');将返回abc，而SELECT Now()利用Now()函数返回当前日期和时间。可以明白如何根据需要使用SELECT进行试验。

## 11 使用数据处理函数

大多数SQL支持的函数：字符串操作、算术操作、处理时间或者日期格式、返回特殊信息

**文本处理函数**

`select vend_name, Upper(vend_name) AS vend_name_upcase from vendors order by vend_name;`

<img src = 'image-6.png' width= 50%>

注意：

表中的SOUNDEX需要做进一步的解释。**SOUNDEX是一个将任何文 本串转换为描述其语音表示的字母数字模式的算法。**

例：

customers表中有一个顾 客Coyote Inc.，其联系名为Y.Lee。但如果这是输入错误，此联系名实 际应该是Y.Lie，怎么办?

```
select cust_name, cust_contact 
from customers 
where Soundex(cust_contact) = Soundex('Y Lie');
```

返回结果：'Y Lee'

**日期和时间处理函数**

<img src = 'image-7.png' width = 50%>

特别说明：

MySQL使用的日期格式：yyyy-mm-dd

Date(order_date)指示MySQL仅提取列的日期部分（例：查询列值为where order_date = '2005-09-01'的行是，只会全值匹配，如果列值为‘2005-09-01 11:30:05’这样的怎么办？应使用Date('2005-09-01')会把包含时间的行查找出来）（为了养成好习惯可以只要查找日期就使用Date()函数）

不过，还有一种日期比较需要说明。如果你想检索出2005年9月下的 所有订单，怎么办?

方法1:

```
select cust_id, order_num 
from orders 
where Date(order_date) between "2005-09-01" and "2005-09-30";
```

方法2:

```
select cust_id, order_num 
from orders 
where Year(order_date) = 2005 and Mouth(order_date) = 9;
```

**数值处理函数**

<img src='image-8.png' width=50%>

##  12 汇总数据

**聚集函数：运行在**行组**上，计算和返回单 个值的函数。**

<img src='image-9.png' width=50%>

SUM()也可以用来合计计算值

例：

`select sum(item_price * quantity) as total_price from oderitems where order_num = 2005`

**在多个列上进行计算 如本例所示，利用标准的算术操作符， 所有聚集函数都可用来执行多个列上的计算。**

NULL值 SUM()函数忽略列值为NULL的行。

**聚集不同值**

DISTINCT(ALL为默认 ALL参数不需要指定，因为它是默认行为。如果 不指定DISTINCT，则假定为ALL。)

`select avg(distinct prod_price) as avg_price from products where vend_id = 1003`

注意：如果指定列名，则DISTINCT只能用于COUNT()。DISTINCT 不能用于COUNT(*)，因此不允许使用COUNT(DISTINCT)， 否则会产生错误。类似地，**DISTINCT必须使用列名**，不能用于计算或表达式。

**组合聚集函数**

```
select count(*) as num_items, min(prod_price) as price_min, max(prod_price) as price_max, avg(prod_price) as price_avg 
from products;
```

## 13 分组数据

**GROUP BY子句和HAVING子句**

**GROUP BY**

`select vend_id, count(*) as num_prods from products group by vend_id;`

表示按照vend_id进行分组，并使用了count()计数字段（计数字段根据组别进行计数，而不是计算总数）

GROUP BY子句指示MySQL分组数据，然后**对每个组而不是 整个结果集进行聚集。**

注意：

1. **GROUP BY子句必须出现在WHERE子句之后，ORDER BY子句之前。**
2. 如果分组列中具有NULL值，则NULL将作为一个分组返回。如果列 中有多行NULL值，它们将分为一组。
3. GROUP BY子句可以**包含任意数目的列**。这使得能对分组进行嵌套， 为数据分组提供更细致的控制。（例：group by vend_id, vend_name）
4. 如果在GROUP BY子句中**嵌套了分组，数据将在最后规定的分组上 进行汇总**。换句话说，在建立分组时，指定的所有列都一起计算
(所以不能从个别的列取回数据)。
5. GROUP BY子句中列出的每个列都必须是**检索列**或**有效的表达式**
(但不能是聚集函数)。**如果在SELECT中使用表达式，则必须在 GROUP BY子句中指定相同的表达式**。不能使用别名。
6. 除聚集计算语句外，SELECT语句中的每个列都必须在GROUP BY子 句中给出。

**HAVING**

WHERE过滤行，而HAVING过滤分组。

HAVING支持所有WHERE操作符

`select cust_id, count(*) as orders from orders group by cust_id having count(*) >= 2;`

WHERE在数据 **分组前**进行过滤，HAVING在数据**分组后**进行过滤

`select vend_id, count(*) as num_prods from products where prod_price >= 10 group by vend_id having count(*) >= 2;`

**分组和排序**

<img src = 'image-10.png' width = 50%>

GROUP BY是分组 **不排序**，所以既分组又排序的话：

`sum(quantity*item_price) as ordertotal from orderitems group by order_num having sum(quantity*item_price) >= 50 order by ordertotal;`

顺序是：where -> group by -> having -> order by
where 按照单个行进行筛选

group by 分组

having 作用于组

order by 排序

**select 子句顺序**

<img src='image-11.png' width=50%>

## 14 使用子查询


子查询： 嵌套在其他查询中的查询

**利用子查询进行过滤**

举例：列出订购物品TNT2的所有客户？

(对于包含订单号、客户ID、 订单日期的每个订单，orders表存储一行。

各订单的物品存储在相关的 orderitems表中。

orders表不存储客户信息。它只存储客户的ID。实际 的客户信息存储在customers表中。)

查询顺序：

1. 检索包含物品TNT2的所有订单的编号。
2.  检索具有前一步骤列出的订单编号的所有客户的ID。 
3.  检索前一步骤返回的所有客户ID的客户信息。

代码：

```
select cust_name, cust_contact
from customers
where cust_id in (select cust_id
					from orders
					where order_num in (select order_num
										from orderitems
										where prod_id = 'TNT2'))
```

保证SELECT语句具有与WHERE子句中相同数目的列

**作为计算字段使用子查询**

显示customers表中每个客户的订单总数。订单与相应的客户ID存储在orders表中?

步骤：
1. 从customers中检索每名客户
2. 对于检索出的每个客户，统计其在orders表中的订单数目

代码：

```
select cust_name, cust_state, 
		(select count(*)
        from orders
        where orders.cust_id = customers.cust_id) as orders
from customers
order by cust_name;
```

完全限定列名:` where orders.cust_id = customers.cust_id`

相关子查询(correlated subquery) 涉及外部查询的子查询。

## 15 联结表

**外键(foreignkey)** 外键为某个表中的一列，它包含另一个表 的主键值，定义了两个表之间的关系。

总之，关系数据可以有效地存储和方便地处理。因此，关系数据库 的可伸缩性远比非关系数据库要好。

**如果数据存储在多个表中，怎样用单条SELECT语句检索出数据? 使用联结**

简单地说，联结是一种机制，用来在一条SELECT 语句中关联表，因此称之为联结。使用特殊的语法，可以联结多个表返 回一组输出，联结在运行时关联表中正确的行。

**创建联结** ：规定要联结的所有表以及它们如何关联即可

```
select vend_name, prod_name, prod_price
from vendors, products
where vendors.vend_id = products.vend_id
order by vend_name, prod_name;
```

WHERE子句的重要性:实际上做 的是将第一个表中的每一行与第二个表中的每一行配对

如果没有where将是 笛卡儿积 的行数 （这样的联结也叫叉联结）

**内部联结**

目前为止所用的联结称为**等值联结(equijoin)**，这种联结也称为**内部联结**

```
select vend_name, prod_name, prod_price
from vendors inner join products on vendors.vend_id = products.vend_id
order by vend_name, prod_name;
```

**与上面的用where的用法相同**

**联结多个表**

```
select prod_name, vend_name, prod_price, quantity
from orderitems, products, vendors
where products.vend_id = vendors.vend_id and
	orderitems.prod_id = products.prod_id and 
    order_num = 20005;
```

上方的三个嵌套子查询可以通过联结表改进为：

```
select cust_name, cust_contact
from customers, orders, orderitems
where customers.cust_id = orders.cust_id
    and orderitems.order_num = orders.order_num
    and prod_id = 'TNT2';
```

## 16 创建高级联结
















































































































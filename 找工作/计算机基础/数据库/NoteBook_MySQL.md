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














































































# ## python 语言从终端输入有几种方式

# 1. inputs()函数 输出为字符串


'''
.split()方法 以空格为分隔符，将字符串分割成列表

int()函数 将字符串转换为整数
'''


user_input = input("请输入： ")

print("你的输入为：", user_input)


# 2. sys模块

import sys

## 1. sys.stdin.readline() 读取一行
user_input = sys.stdin.readline()
print("你的输入为：", user_input)

## 2. sys.stdin.readlines() 读取多行
user_input = sys.stdin.readlines()
print("你的输入为：", user_input)

## 3. sys.stdin.read() 读取所有
user_input = sys.stdin.read()
print("你的输入为：", user_input)

## 4. sys.stdin.read(1) 读取一个字符
user_input = sys.stdin.read(1)
print("你的输入为：", user_input)

## 5. 命令行参数 sys.argv
print("脚本名：", sys.argv[0])
print("参数：", sys.argv[1:])
print("参数个数：", len(sys.argv))

## 6. sys.stdin()
input = sys.stdin()
print("你的输入为：", input)

# 3. 文件读取

with open(file_path, "r") as file:

    ## 1. 读取一行
    user_input = file.readline()
    print("你的输入为：", user_input)

    ## 2. 读取多行
    user_input = file.readlines()
    print("你的输入为：", user_input)

    ## 3. 读取所有
    user_input = file.read()
    print("你的输入为：", user_input)

    ## 4. 读取一个字符
    user_input = file.read(1)
    print("你的输入为：", user_input)

## 5. 读取字节流
    
    with open(file_path, "rb") as file:
        user_input = file.read()
        print("你的输入为：", user_input)

        # 每次读取指定字节数的字节流
        chunk = file.read(chunk_size)
    







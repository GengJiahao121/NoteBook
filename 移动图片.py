'''
!!!注意此代码只能运行一次！！！要不然就会叠加picture路径名
'''


import os
import re

# Markdown文件路径
markdown_file = "NoteBook_MySQL.md"
# 图片文件夹路径
image_folder = "picture/"

# 提取图片路径的正则表达式
image_regex1 = r"'([^']*.png)'" # 匹配<img src='*.png'>
image_regex2 = r"\(([^)]*\.png)\)" # 匹配![](*.png)

# 读取Markdown文件内容
with open(markdown_file, "r") as file:
    content = file.read()

# 查找所有的图片路径
image_paths1 = re.findall(image_regex1, content)
image_paths2 = re.findall(image_regex2, content)
image_paths = image_paths1 + image_paths2
print(image_paths)

# 遍历每个图片路径
for image_path in image_paths:
    # 提取文件名
    image_filename = os.path.basename(image_path)
    # 生成新的图片路径
    new_image_path = os.path.join(image_folder, image_filename)
    # 替换Markdown文件中的图片路径
    content = content.replace(image_path, new_image_path)

# 将更新后的内容写入Markdown文件
with open(markdown_file, "w") as file:
    file.write(content)
"""
作者：Coco
日期：2021年07月26日
"""

name = 'boB'
sex = 'man'
hobby = ' ball '
# 字符串常用函数
# 首字母大写 title()
print(name.title())
# 全部大写 upper()
print(name.upper())
# 全部小写 lower()
print(name.lower())
# 字符串拼接
person = f'{name}是{sex}'
print(person)
# 删除末尾空白(只是展示删除，原来的变量没有变)
print(hobby)
hobby_rstrip = hobby.rstrip()
print(hobby_rstrip)
# 删除开头的空白(只是展示删除，原来的变量没有变)
hobby_lstrip = hobby.lstrip()
print(hobby_lstrip)
# 删除首尾的空白(只是展示删除，原来的变量没有变)
hobby_strip = hobby.strip()
print(hobby_strip)


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
# 在字符串中使用变量
person = f'{name}是{sex}'
people = "{}是{}".format(name, sex)
print(person)
print(people)
# 删除末尾空白(只是展示删除，原来的变量没有变;要永久删除空白，必须将删除的结果关联到变量)
print(hobby)
hobby_rstrip = hobby.rstrip()
print(hobby_rstrip)
# 删除开头的空白(只是展示删除，原来的变量没有变)
hobby_lstrip = hobby.lstrip()
print(hobby_lstrip)
# 删除首尾的空白(只是展示删除，原来的变量没有变)
hobby_strip = hobby.strip()
print(hobby_strip)
# 正向查找子字符串，找到返回的值>=0没找到返回-1
result = name.find('b')
result2 = name.find('c')
print(result)
print(result2)
# 统计在原字符串中出现的次数
count = hobby.count('l')
print(count)
# 获取字符串的长度
length = len(hobby)
print(length)
# split()分割
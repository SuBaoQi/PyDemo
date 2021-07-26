"""
作者：Coco
日期：2021年07月26日
"""
name = 'bOb'
sex = 'man'
hobby = ' ball '
# 字符串常用函数
# 首字母大写
print(name.title())
# 全部大写
print(name.upper())
# 全部小写
print(name.lower())
# 字符串拼接
person = f'{name}是{sex}'
print(person)
# 删除末尾空白
print(hobby)
hobby_rstrip = hobby.rstrip()
print(hobby_rstrip)
# 删除开头的空白
hobby_lstrip = hobby.lstrip()
print(hobby_lstrip)
# 删除首尾的空白
hobby_strip = hobby.strip()
print(hobby_strip)

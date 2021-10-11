"""
作者：Coco
日期：2021年10月03日
"""
'''
将字符串中单词的位置反转， “hello xiao mi”转化为“mi xiao hello”
'''
# s = "hello xiao mi"
# s_split = s.split(" ")
# print(s_split)
# s_split.reverse()
# print(s_split)
# s_join = " ".join(s_split)
# print(s_join)
'''
打印100遍hello python，第50遍不打印
'''
# index = 1
# while index < 101:
#     if index == 50:
#         index += 1
#         continue
#     print("hello python")
#     print(index)
#     index += 1
'''
打印九九乘法表
1*1=1
1*2=1 2*2=4
1*3=3 2*3=6 3*3=9
'''
# for column in range(1, 10):
#     for row in range(1, column + 1):
#         print(f"{row}*{column}={row * column}", end=' ')
#     print()
'''
实现把字符串 st_r='woaixuexi'中的任意小写变成大写输出（通过输入函数完成）
'''
# st_r = "woaixuexi"
# value = input("请输入您要转化的字母：")
# value_upper = value.upper()
# print(st_r.replace(value, value_upper))

'''
分别打印10以内的所有偶数和奇数，并存入不同的列表当中
'''
# oushu = []
# jishu = []
# for value in range(0, 11):
#     print(value)
#     if value % 2 == 0:
#         oushu.append(value)
#     else:
#         jishu.append(value)
# print(oushu, jishu)
'''
请写一段代码实现删除一个列表中list=[1,3,6,9,1,8] 重复的元素
'''
# li_st = [1, 3, 6, 9, 1, 8]
# result = list(set(li_st))
# print(result)
'''
把字符串 user_controller转化为驼峰命名UserController
'''
# result = []
# value = 'user_controller'
# value_split = value.split('_')
# for vs in value_split:
#     print(vs)
#     vs_title = vs.title()
#     result.append(vs_title)
# print(result)
# join = ''.join(result)
# print(join)
'''
python实现斐波那契
'''

value = int(input("想要几位斐波那契数列："))

li_st = []
for i in range(value):
    if i == 0 or i == 1:
        li_st.append(1)
    else:
        li_st.append(li_st[i - 2] + li_st[i - 1])
print(li_st)

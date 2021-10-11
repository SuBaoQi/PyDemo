"""
作者：Coco
日期：2021年07月21日
"""
# 定义一个列表
student = ['小明', '小红', '小刚']
# print(student)
# # 增删改查
# # 查
# print(student[0])
# print(student[-1])
# # 改
# index = student.index('小明')
# student[index] = '改造小明'
# print(student)
# # 增
# # 末尾追加
# student.append("新增01")
# print(student)
# # 制定位置新增
# student.insert(3, "新增02")
# print(student)
# # 合并列表
# student02 = ["张三"]
# student.extend(student02)
# print(student)
# # 删
# del student[0]
# print(student)
# # 弹出（默认弹出最后一位）
# student_pop = student.pop()
# print(student_pop)
# student_pop02 = student.pop(0)
# print(student_pop02)
# # 根据值删除
# print(student)
# student.remove('小刚')
# print(student)
# # 组织列表
# 按照顺序对列表进行永久排序
cars = ['bmw', 'toyota', 'audi', 'subaru']
# cars.sort()
# print(cars)
# # 相反顺序对列表进行永久排序
# cars.sort(reverse=True)
# print(cars)
# # 对列表进行临时排序
# print(sorted(cars))
# print(cars)
# # 对列表进行翻转
# cars.reverse()
# print(cars)
# # 确定列表的长度
# print(len(cars))
# # 遍历
for car in cars:
    print(car)
# # 对数字列表进行统计计算
# value = list(range(10))
# print(min(value))
# print(max(value))
# print(sum(value))
# # 切片
# print(cars[0:1])
# # 复制列表
# car02 = cars[:]
# print(cars)
# print(car02)
# car02.append("aaa")
# print(cars)
# print(car02)

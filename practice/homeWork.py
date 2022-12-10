# 打印5行5列的正方形，单元格中使用*号进行填充
def fun1():
    i = 1
    while i <= 5:
        j = 1
        while j <= 5:
            print('*', end="")
            j += 1
        print('')
        i += 1


# 打印直角三角形
def fun2():
    i = 1
    while i <= 5:
        j = 1
        while j <= i:
            print('* ', end='')
            j += 1
        print('')
        i += 1


# 打印9*9乘法表
def fun3():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f'{j}*{i}={i * j} ', end='')
            j += 1
        print('')
        i += 1


# 求1-100的和
def fun4():
    result = 0
    for i in range(1, 101):
        result += i
    print(result)


# 求1-100之间的偶数的和
def fun5():
    result = 0
    for i in range(1, 101):
        if i % 2 == 0:
            result += i
    print(result)


# 有一个数字，不知道具体是多少，用3去除剩2，用5去除剩3，用7去除剩2，问这个数是多少1-100以内的整数
def fun6():
    for i in range(1, 101):
        if i % 3 == 2:
            if i % 5 == 3:
                if i % 7 == 2:
                    print(i)


def fun7():
    for i in range(1, 101):
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
            print(i)


# 报数字，一些同学从1开始报数，当需要报出的数字尾数是7或者该数字是7的倍数时，则该同学跳过这个数字，不进行报数。所有的同学都参与游戏后，游戏结束。如输入学生
# 数量是50，游戏结束后，报数的同学数量为39。
def fun8(renshu):
    count = 0
    for i in range(1, renshu + 1):
        if i % 7 == 0 or i % 10 == 7:
            continue
        else:
            count += 1
    print(count)
# 使用循环嵌套打印正等腰三角形
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
if __name__ == '__main__':
# 1111111
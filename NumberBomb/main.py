# -*- coding: utf-8 -*-
# @Time    : 2026/4/25 10:17
# @Author  : 檐思辙
# @FileName: main.py
# @Software: PyCharm

import random


# 二分搜索算法
def binary_search(res):
    count_theory_value = 0
    left = 1
    right = 100
    list = []
    while 1:
        mid = (left + right) // 2   # 去掉小数部分
        count_theory_value += 1
        list.append(mid)
        if mid < res:
            left = mid + 1
        elif mid > res:
            right = mid - 1
        elif mid == res:
            break
    return count_theory_value, list


res = random.randrange(1, 100)
number = 0
count_user = 1
left = 1
right = 100
while 1:

    print(f"第{count_user}次猜炸弹,范围在[{left},{right}]:", end="")

    try:
        number = int(input())
    except ValueError:
        print(f"错误输入！请输入[{left},{right}]的数字")
        continue

    # 判断数字是否在有效范围之间
    if number > right:
        print("数字超出有效范围")
        continue
    elif number < left:
        print("数字小于有效范围")
        continue

    count_user += 1   # 计次数
    if number < res:
        print("数字小了")

        left = number + 1
    elif number > res:
        print("数字大了")
        right = number-1
    elif number == res:
        print("猜对了")
        break
count_user -= 1
print(f"您一共进行了{count_user}次猜数字的环节")
count_theory_value, theory_list = binary_search(res)
print(f"采用二分搜索算法需进行{count_theory_value}次")
print(f"查找值为：{theory_list}")

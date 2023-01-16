"""
【问题描述】
设计一个简易的整数计算器。
【输入格式】
三行，第一行是一个数字，第二行是符号（+、-、*、/），第三行是数字。
【输出格式】
一个整数
【样例输入】
7
*
9
【样例输出】
63
"""

# 输入数据
int1 = eval(input())
symbol_12 = input()
int2 = eval(input())

# 处理数据（输出结果）
if symbol_12 == '+':
    print(int1 + int2)
elif symbol_12 == '-':
    print(int1 - int2)
elif symbol_12 == '*':
    print(int1 * int2)
else:
    print(int1 / int2)

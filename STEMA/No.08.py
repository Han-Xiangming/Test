"""
【问题描述】
输入一行字符，分别统计出其英文字母、空格、数字和其它字符的个数并输出。
【输入格式】
输入一行字符
【输出格式】
按英文字母、空格、数字和其它字符的顺序输出其对应的个数
【样例输入】
a1 b2 c d4 !!! 5
【样例输出】
4
5
4
3
"""

# 输入数据
S = input()

# 处理数据
abc = space = digit = other = 0
for i in S:
    if i.isalpha():
        abc += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        other += 1

# 输出结果
print(abc)
print(space)
print(digit)
print(other)

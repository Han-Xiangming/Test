"""
【问题描述】
某考试系统要根据学生年龄限制不同组别：
 年龄在6-12岁，会自动分配“小学组”（包括6和12）
 年龄13至15岁，分配“中学组”（包括13和15）
 年龄16至18岁，分配“高中组”（包括16和18）
请你编写程序，实现输入学生年龄，提示学生组别的功能。
【输入格式】
一行，一个整数，表示学生年龄
【输出格式】
一行，输出对应的组别，“小学组”、“中学组”或“高中组”
【样例输入】
13
【样例输出】
中学组
"""

# 输入数据
age = eval(input())

# 处理数据（输出结果）
if 6 <= age <= 12:
    print('小学组')
elif 13 <= age <= 15:
    print('中学组')
else:
    print('高中组')
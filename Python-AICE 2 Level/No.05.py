"""
【题目描述】
心脏是人体最为重要的一个器官，心脏跳动的快慢和身体健康有非常密切的关系，检测到心率低于60次/分钟，则“心跳慢”；心率在60到100次/分钟之间（包括60和100），属于“正常”；如果心率高于100次/分钟，则“心跳快”。
请你帮忙做一个检测心率的程序，实现输入心率，提示心跳的情况。
【输入格式】
一行，一个整数，表示心率
【输出格式】
一行，输出对应的结果，“心跳慢”、“正常”或“心跳快”
【样例输入】
100
【样例输出】
正常
"""

# 输入数据
heart_rate = eval(input())

# 处理数据（输出结果)
if heart_rate < 60:
    print('心跳慢')
elif 60 <= heart_rate <= 100:
    print('正常')
else:
    print('心跳快')

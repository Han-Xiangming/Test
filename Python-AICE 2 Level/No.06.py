"""
【问题描述】
某点评app要为某区域的餐厅做特别推广，现需收集所有参与活动的餐厅信息，请你编写程序，制作一个餐厅录入系统，需求如下：
【功能需求】
该系统可以多次录入餐厅信息，每次录入餐厅名称后，都将这家餐厅名称添加到列表中；如果输入“结束”，则打印总列表清单，并结束程序。
【输入格式】
一行，表示输入的餐厅名称
【输出格式】
一个列表，根据情况输出列表
【样例输入】
老北京烤鸭
魏家凉皮
结束
【样例输出】
['老北京烤鸭','魏家凉皮']
"""

# 输入数据（处理数据，输出结果）
dining = []
while True:
    Name = input()
    if Name == '结束':
        print(dining)
        break
    else:
        dining.append(Name)

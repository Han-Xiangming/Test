"""
【编程实现】
某比赛对学生的成绩进行级别的区分，如果学员的成绩大于等于90分，则获得成绩A，80到90之间（包含80），
则获得成绩B，如果学员的成绩在70到80之间（包含70）则获得成绩C，
如果学员成绩在60到70之间（包含60）则获得成绩D，小于60分则获得成绩E。请你编写一个程序实现自动化打印成绩。
【输入数据】
一行，一个整数表示输入的成绩
【输出数据】
一行，一个字母表示输出的结果
【样例输入】
90
【样例输出】
A
"""
n = eval(input())
if n >= 90:
	print('A')
elif n >= 80:
	print('B')
elif n >= 70:
	print('C')
elif n >= 60:
	print('D')
else:
	print('E')

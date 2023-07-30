"""
输入两个正整数a和b，输出它们的最大公约数。
公约数，指能被两个数同时整除的一些数。
最大公约数就是这些数中的最大值。
例如：a=96，b=50，最大公约数是2。
【输入数据】
两行，两个正整数a 和b(2<=a，b<=1000)
【输出数据】
一行，两个数字的最大公约数
【样例输出】
96
50
【样例输出】
2
"""


a = eval(input())
b = eval(input())
smaller = min(a, b)
for i in range(smaller, 0, -1):
	if (a % i == 0) and (b % i == 0):
		print(i)
		break

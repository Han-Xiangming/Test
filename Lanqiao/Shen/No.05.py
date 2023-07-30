"""
【编程实现】
质数：是指这个数只能被1和它自己本身整除的数
输入两个整数a,b(a,b>2),请你输出a,b之间的所有的质数。
【输入数据】
一行，两个整数，中间用空格隔开
【输出数据】
一行，输出结果中间用逗号隔开
【样例输入】
3 11
【样例输出】
3,5,7,11
"""

s = [int(i) for i in input().split(' ')]
a, b = s[0], s[1]
if a > b:
	a, b = b, a
num = []
for i in range(a, b + 1):
	bl = next((0 for j in range(2, i) if i % j == 0), 1)
	if bl != 1:
		continue
	num.append(i)
for i in range(len(num) - 1):
	print(num[i], end=',')
print(num[-1])

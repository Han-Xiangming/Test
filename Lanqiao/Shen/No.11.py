"""
【编程实现】
输入两个数字a，b，输入一个运算符号s，运算符号从加+、减-、乘*、除/、取余%五种任取一种，根据所选运算符号计算它们最终的结果。如果是加法，则计算它们两个相加后的结果；例如：a=3，b=5，s="+"，结果为8。
运算符号：
+，加法运算
-，减法运算
*，乘法运算
/，取整运算
%，取余运算
【输入数据】
三行，两个数字a，b，一个运算符号s
【输出数据】
一行，两个数字运算后的结果
【样例输入】
3
5
+
【样例输出】
8
"""
a = eval(input())
b = eval(input())
c = input()
if c == '+':
	print(a + b)
elif c == '-':
	print(a - b)
elif c == '*':
	print(a * b)
elif c == '/':
	print(a / b)
elif c == '%':
	print(a % b)

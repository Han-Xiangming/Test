"""
【编程实现】
请你编写一个程序实现：将英文单词的后缀（er、ly、ing）删除，如果英文单词的后缀没有这三种，就输出原有的英文单词。
【输入数据】
一行，一串字符串表示英文单词
【输出数据】
一行，一串处理后的结果
【样例输入】
instrumenting
【样例输出】
instrument
"""

s = input()
if 'er' in s or 'ly' in s:
	s = s[:-2]
elif 'ing' in s:
	s = s[:-3]
print(s)

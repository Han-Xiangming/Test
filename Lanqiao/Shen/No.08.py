"""
【编程实现】
给你一个字符串a和一个正整数n，判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：字符串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba"。
【输入数据】
两行，第一行为输入的字符串，第二行为一个整数表示长度n
【输出数据】
一行字符串，表示判断的结果
示例一
输入：
tdabcbaef
3
输出：
YES
"""

a = input()
n = eval(input())
for i in range(len(a) - n + 1):
	s = a[i:i + n]
	if s != s[::-1]:
		jg = "NO"
	else:
		jg = "YES"
		break
print(jg)

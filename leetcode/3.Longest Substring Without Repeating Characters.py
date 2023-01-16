"""
【题目描述】
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
【示例】
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

s = input()
sl, c = [], []
sl.extend(iter(s))
for i in range(len(sl)):
    if sl[i] == sl[i + 1]:
        c.clear()
    c.append(sl[i])

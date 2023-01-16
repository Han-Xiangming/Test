"""
[题目描述】
给你一个字符串s，找到s中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
【示例1】
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
【示例2】
输入：s = "cbbd"
输出："bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        length = len(s)
        li = [[False for x in range(length)] for x in range(length)]
        for j in range(length):
            for i in range(j + 1):
                if j - i in [0, 1, 2] and s[i] == s[j]:
                    li[i][j] = True
                else:
                    li[i][j] = (li[i + 1][j - 1]) and (s[i] == s[j])

                if li[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    maxstr = s[i:j + 1]
        return maxstr

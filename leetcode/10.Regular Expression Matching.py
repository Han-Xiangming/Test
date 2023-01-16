"""
【问题描述】【难度：困难】
给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
【示例1】
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
【示例2】
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        canfind = re.findall(p, s)
        if len(canfind) == 0:
            return False
        else:
            for i in canfind:
                if i == s:
                    return True
            return False

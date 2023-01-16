"""
【题目描述】【难度：简单】
给你两个二进制字符串a和b，以二进制字符串的形式返回它们的和。
【示例】
输入: a = "11", b = "1"
输出: "100"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

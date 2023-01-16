"""
【题目描述】【难度：简单】
给你一个整数x，如果x是一个回文整数，返回true；否则，返回false。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
【示例1】
输入：x = 121
输出：true
【示例2】
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

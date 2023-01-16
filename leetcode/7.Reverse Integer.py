"""
【题目描述】
给你一个32位的有符号整数x，返回将x中的数字部分反转后的结果。
如果反转后整数超过32位的有符号整数的范围[−231,231−1]就返回0。
假设环境不允许存储64位整数（有符号或无符号）。
【示例】
输入：x = 123
输出：321
"""


class Solution:
    def reverse(self, x: int) -> int:
        sws = []
        for i in str(abs(x)):
            sws.insert(0, i)
        sws = ''.join(sws)
        if int(sws) > 2 ** 31 - 1:
            return 0
        elif x < 0:
            return -int(sws)
        else:
            return int(sws)

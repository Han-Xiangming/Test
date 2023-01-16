"""
【题目描述】【难度：中等】
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以0开头。
【示例】
输入：l1 = [2,4,3],l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807
"""


def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    l1_int = int("".join(list(map(str, l1))))
    l2_int = int("".join(list(map(str, l2))))
    l3_str = str(l1_int + l2_int)
    l3 = [int(i) for i in l3_str]
    l3.reverse()
    return l3

"""
【题目描述】【难度：中等】
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
【示例】
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hash_set = set()
        left = 0
        for right, ch in enumerate(s):
            while ch in hash_set:
                hash_set.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            hash_set.add(ch)
        return ans

"""
LCR 119. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（序列元素在原数组中连续）的长度。
示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""


def longestConsecutive(nums):
    if not nums:
        return 0
    nums = list(set(nums))
    nums.sort()
    max_streak = 1
    current_streak = 1
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1
    return max_streak


print(longestConsecutive([int(i) for i in input().split()]))

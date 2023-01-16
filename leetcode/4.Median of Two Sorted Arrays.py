"""
【问题描述】【难度：困难】
给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数。
算法的时间复杂度应该为 O(log (m+n)) 。
【示例1】
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
【示例2】
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        arr = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        arr += nums1[i:m]
        arr += nums2[j:n]
        # while i < m:
        #     arr.append(nums1[i])
        #     i += 1
        # while j < n:
        #     arr.append(nums2[j])
        #     j += 1

        arr_length = len(arr)
        if arr_length % 2:
            result = arr[arr_length // 2]
        else:
            result = (arr[arr_length // 2 - 1] + arr[arr_length // 2]) / 2

        return round(result, 5)

"""
在已知的一组整数中，有这样一种数非常奇怪，它们不在第一个，
也不在最后一个，
而且刚好比左边和右边相邻的数都大，这种数叫做支撑数。
请你编写程序，输入一组整数，输出每个支撑数的数值以及它们在数组中的位置编号。
例如：对于一组整数：1, 4, 2。支撑数是4，它在整数数组中的位置编号为2。
【输入格式】输入一组整数，整数之间用英文逗号隔开。
【输出格式】按行依次输出每个支撑数的数值和它们在数组中的位置编号（每一行的支撑数和位置编号中间用空格隔开），如果不存在支撑数则输出-1。
输入：
1,2,3,4
输出：
-1

输入：
1,3,2,4,3
输出：
3 2
4 4
"""

def solution(array):
    result = []
    if len(array) <= 2:
        return -1
    else:
        for i in range(1,len(array)-1):
            if array[i] > array[i-1] and array[i] > array[i+1]:
                result.append(i)
    if len(result) == 0:
        return -1
    return result
l = list(map(int,input().split(',')))
result = solution(l)
if result == -1:
    print('-1')
else:
    for i in result:
        print(f"{l[i]} {i+1}")
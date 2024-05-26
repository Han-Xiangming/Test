"""
【题目描述】
小张在一家电影院工作，每天都需要统计不同电影的观影人数，并将观影人数按照从高到低的顺序录入电影院系统。已知程序要求如下，请你编写程序实现该功能。
（1）在一行中输入每部电影的观影人数，中间用空格隔开。
（2）使用选择排序算法，对每部电影的观影人数进行从高到低排序，将观影人数保存在列表中并打印出来。
【输入格式】
 在一行输入每部电影的观影人数，中间用空格隔开
【输出格式】
输出一个列表，列表中保存的是从高到低排序后的电影观影人数
【样例输入】
10 20 40
【样例输出】
[40,20,10]
"""
def bubble_sort(a):
    array = [int(num) for num in a.split(' ')]
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

input_str = input()
sorted_array = bubble_sort(input_str)
print(sorted_array)

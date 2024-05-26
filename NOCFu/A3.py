"""
分别输入两个正整数m、n（m<n），请统计m到n之间所有整数（含m和n本身）中，个位为3的整数的数量。例如，m和n为1和20，那么在这个范围内，
个位为3的数字有2个，即3和13，因此满足条件的整数有2个。
【输入格式】输入一行，包括两个正整数m、n，
整数之间使用空格隔开（m和n均小于10000）。
【输出格式】输出一个整数，
表示m到n之间（包含m和n）所有整数中个位为3的整数的数量。
【样例输入】
1 20
【样例输出】
2
"""
m, n = map(int, input().split())
count = 0
for i in range(m, n + 1):
    if i % 10 == 3:
        count += 1
print(count)
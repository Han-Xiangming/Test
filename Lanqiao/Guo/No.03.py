"""
【题目描述】
壮猿在运送物资的时候，遇到了一条大河，要想将物资运送过去，必须请小马进行帮忙，已知小马每次只能运算1件或2件物资，现在壮猿有n件物资要运送，一共有多少种运送方案呢？
【输入格式】
一个整数，表示要运送的n件物资
【输出格式】
一个整数，表示运送方案的总数
【样例输入】
8
【样例输出】
34
"""
n = eval(input())


def f(n):
    if n == 1:
        return 1
    return 2 if n == 2 else f(n - 1) + f(n - 2)


print(f(n))
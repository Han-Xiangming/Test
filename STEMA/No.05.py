"""
【提示信息】
倍数与约数：如果a能被b整除，a就叫做b的倍数，b就叫做a的约数。约数和倍数都表示一个整数与另一个整数的关系，不能单独存在。
最大公约数：几个整数中公有的约数，叫做这几个数的公约数；其中最大的一个，叫做这几个数的最大公约数。
举例：12、16的公约数有1、2、4，其中最大的一个是4，所以4是12与16 的最大公约数。
最小公倍数：几个自然数公有的倍数，叫做这几个数的公倍数，其中最小的一个，叫做这几个数的最小公倍数。
举例：4的倍数有4、8、12、16，……，6的倍数有6、12、18、24，……，4 和6的公倍数有12、24，……，其中最小的是12，所以4和6最小公倍数为12。
【问题描述】
分别输入两个正整数(1<正整数<201)，输出这两个正整数的最大公约数M及最小公倍数N(注：M和N之间以一个英文逗号隔开)。
【输入格式】
    第1行输入第一个正整数
	第2行输入第二个正整数
【输出格式】
输出这两个正整数的最大公约数M及最小公倍数N(M和N之间以一个英文逗号隔开)
【样例输入】
4
6
【样例输出】
2,12
"""

# 输入数据
I1 = eval(input())
I2 = eval(input())


# 处理数据
def gcd(a, b):
    biggest = a if a > b else b
    for i in range(biggest + 1):
        if a % (biggest - i) == 0 and b % (biggest - i) == 0:
            return biggest - i


def lcd(a, b):
    biggest = a if a > b else b
    while True:
        if biggest % a == 0 and biggest % b == 0:
            return biggest
        biggest += 1


M = gcd(I1, I2)
N = lcd(I1, I2)

# 输出结果
print(M, end=',')
print(N)
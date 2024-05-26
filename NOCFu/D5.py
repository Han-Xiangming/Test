"""
质数是指一个数字除了1和它本身之外，没有其他因数，这样的数字是质数。（注意：1不是质数）
现在给定一个整数n，请你编写程序计算1～n（包含1和n）之间的所有质数的和。
【输入格式】输入一个整数（1<整数<=1000）。
【输出格式】输出一个整数，表示1～n（包含1和n）之间的所有质数的和。
输入：
10
输出：
17
"""
sum = 0
def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
for i in range(1,int(input())+1):
    if isprime(i):
        sum += i
print(sum-1)
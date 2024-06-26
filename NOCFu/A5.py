"""
学校组织一场游戏，游戏中需要学生进行两两组队，每个学生都有唯一的数字ID，
如果A同学ID的因数（该因数不包括这个数本身）之和恰好等于B同学的ID，
并且B同学ID的因数（该因数不包括这个数本身）之和恰好等于A同学的ID。那么这两个人就可以组队成功。
现在请你编写程序实现根据两个同学的ID，判断这两位同学是否能组队成功。
【输入格式】：输入一行，包含两个整数（两个整数不相等），中间用空格隔开，分别表示两个同学的ID。
【输出格式】：如果两个同学能组队成功，则输出“Y”，否则输出“N”。
【样例输入】
220 284
【样例输出】
Y
"""
def f(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    return sum
a,b = map(int,input().split())
sa,sb  = f(a),f(b)
print("Y" if sa == b and a == sb else "N")
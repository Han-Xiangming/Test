"""
老师想要将一堆糖果平均分给三个小朋友（糖果不能被分割），现在请你帮助老师判断是否可以平均分配这些糖果呢？
【输入格式】输入一个整数，代表老师的糖果数量。
【输出格式】如果可以平均分配这些糖果则输出"YES"，否则输出"NO"。
"""
print('YES' if int(input()) % 3 == 0 else 'NO')
"""
输入三个整数n，m，k，其中n<m，从n～m（包含n和m）中取出两个整数i和j，统计满足i+j=k的组合数量（i+j=k和j+i=k是两种组合）。
【输入格式】输入三个整数n，m，k，其中n<m（m<=1000），整数之间用空格隔开。
【输出格式】输出满足i+j=k的组合数量（i+j=k和j+i=k是两种组合）
输入：
20 100 50
输出：
11
"""
s = [int(i) for i in input().split()]
n,m,k = s[0],s[1],s[2]
cnt = 0
for i in range(n,m+1):
    for j in range(n,m+1):
        if i+j == k:
            cnt += 1
print(cnt)
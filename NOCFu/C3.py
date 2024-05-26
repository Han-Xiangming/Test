"""
输入一个字符串（字符串中不包含空格），请编写程序将字符串中的所有数字字符（0-9）移动到字符串的末尾，同时保持它们的原始顺序。例如：将字符串"hello,123world987"变成"hello,world123987"。
【输入格式】输入一个字符串（字符串中不包含空格）。
【输出格式】将字符串中的所有数字字符（0-9）移动到字符串的末尾，同时保持它们的原始顺序并输出。
输入：
a1b2c3
输出：
abc123
输入：
18岁
输出：
岁18
"""
s = input()
nums = []
chars = []
for i in range(len(s)):
    if s[i].isdigit():
        nums.append(s[i])
    else:
        chars.append(s[i])
print(''.join(chars)+''.join(nums))
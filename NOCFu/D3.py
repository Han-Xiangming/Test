"""
小强英语课上学完五个元音字母a，e，i，o，u之后，他想要知道一个字符串中共有多少个元音字母，请你编写程序帮助小强统计字符串中元音字母的个数。
【输入格式】输入一行，一个字符串。
【输出格式】输出一个整数，表示元音字母的个数。
输入：
aeiou
输出：
5
"""
def dayan(s):
    cnt = 0
    y = 'aeiouAEIOU'
    for i in s:
        if i in y:
            cnt += 1
    return cnt


print(dayan(input()))
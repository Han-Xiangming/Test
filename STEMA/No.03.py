"""
【问题描述】
小蓝的学校组织了一场演讲比赛，有8位评委对参赛选手进行打分。
打分规则是去掉8位评委中最高分和最低分后，计算出剩余6位评委分数的平均值（保留两位小数）作为最后得分。
小蓝同学也积极参加了本次演讲比赛，请你帮小蓝计算一下她的最后得分。
输入8个整数（0<=输入整数<=100）分别以逗号隔开作为8位评委对小蓝同学的打分，请按照打分规则计算出小蓝的最后得分并输出。
【输入格式】
输入8个整数（0<=输入整数<=100），分别以逗号隔开
【输出格式】
输出小蓝的最后得分（注意，保留两位小数）
【样例输入】
50,90,55,78,52,68,66,93
【样例输出】
68.17
"""

# 输入数据
Score = input()

# 处理数据
Temp_Score_list = Score.split(',')
Score_list = [int(i) for i in Temp_Score_list]
Score_list.remove(max(Score_list))
Score_list.remove(min(Score_list))

# 输出结果
print('%.2f' % (sum(Score_list) / len(Score_list)))

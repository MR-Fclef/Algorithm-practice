# # -*- coding: utf-8 -*-
import sys

# inp = raw_input().split(';')
# user = raw_input()
# print inp
# print user
# dic = {}
# for i in range(len(inp)):
#     m = inp[i].split("_")
#     shuxing = m[0]
#     text = m[1].split('|')
#     if shuxing not in dic:
#         dic[shuxing] = text
# reload(sys)
# sys.setdefaultencoding("utf-8")
# print dic

# data = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
# #利用参数key来规定排序的规则
# result = sorted(data,key=lambda x:(x[1].lower(),x[0]))

# print(data) #结果为 [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
# print(result) #结果为 [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]


arr = []
index = 0
huancun = []
for i in range(1000000):
    inp = sys.stdin.readline().split(' ')
    if inp[0] == '\n':
        break
    index  += int(inp[0])
    for j in range(int(inp[0])):
        huancun.append(int(inp[j+1]))
    huancun.sort()
    # print(huancun)
    arr.append(huancun[int(index/2)])
    # print(arr)
for i in range(len(arr)):
    print(arr[i])
        


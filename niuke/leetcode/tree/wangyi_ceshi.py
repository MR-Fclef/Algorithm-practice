

# 本题为考试多行输入输出规范示例，无需提交，不计分。
#coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     print(n)
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         print(line)
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         print(values)
#         for v in values:
#             ans += v
#     print(ans)

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     a = sys.stdin.readline().strip() 
#     n = a[0]
#     k = a[2]
#     t = []
#     ans = 0
#     Max = 0
#     m = 0
#     for i in range(2):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # print(line)
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         t.append(values)
#         # print(values)
#     # print(t)
#     for i in range(int(n)):
#         if t[1][i]==1:
#             ans += t[0][i]
#         if t[1][i]==0:
#             m = 0
#             for j in range(3):
#                 if(i+j)<int(n):
#                     if t[1][i+j]==0:
#                         m += t[0][i+j]
#                 continue
#         # print(m)
#         Max = max(Max,m)
#     # print(ans)
#     print(Max+ans)

#     #     for v in values:
#     #         ans += v
#     # print(ans)

# import sys 
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))



import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    res = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        values.append(i+1)
        res.append(sorted(values))
    print(res)
    for i in range(n):
        for j in range(1，len(res[i])):
            if res[i][j] in res[i+1]:
                res[i] = res[i] + res[i+1]


    
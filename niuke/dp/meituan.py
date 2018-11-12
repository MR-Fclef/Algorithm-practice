# import sys
# m = int(sys.stdin.readline())
# print(m)


import sys

m = list(sys.stdin.readline().split(' '))
n = list(sys.stdin.readline().split(' '))
m_len = int(m[0])
k = int(m[1])
n = [int(n[i]) for i in range(m_len)]

print(m_len)
print(k)
print(n)
dis = 0
Max = 0
index_0 = []
for i in range(m_len):
    if n[i]==0:
        index_0.append(i)

for j in range(m_len):
    if n[j]==1:
        dis += 1 
        Max  = max(Max,dis)
    else:
        dis = 0


#1 0 0 1 0 1 0 1 0 1
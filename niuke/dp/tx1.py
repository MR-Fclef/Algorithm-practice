import sys

k = int(sys.stdin.readline())
A = sys.stdin.readline()
B = sys.stdin.readline()
A = A[0:len(A)-1]
B = B[0:len(B)-1]

dic_num = {}
zichuan_set = []
for i in range(len(A)-k+1):
    if A[i:i+k] not in zichuan_set:
        zichuan_set.append(A[i:i+k])
        dic_num[A[i:i+k]] = 0
print(zichuan_set)

res = 0
for i in range(len(B)-k+1):
    if B[i:i+k] in dic_num:
        res += 1

print(res)


import sys

inp1 = sys.stdin.readline().split(' ')
N = int(inp1[0])
M = int(inp1[1])
P = int(inp1[2])
# print(N,M,P)

inp2 = sys.stdin.readline().split(' ')
A = []
for i in range(N):
    A.append(int(inp2[i]))
# print(A)
arr= []
for i in range(M):
    inp3 = sys.stdin.readline().split(' ')
    arr.append(inp3)
# print(arr)

for i in range(M):
    if arr[i][0] == 'A':
        A[int(arr[i][1])-1] += 1
    if arr[i][0] == 'B':
        A[int(arr[i][1])-1] -= 1
# print(A)
value = A[P-1]
A.sort()
A.reverse()
for i in range(N):
    if A[i] == value:
        print(i+1)
        break




import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    inp = sys.stdin.readline().split(' ')
    huancun = []
    for i in range(len(inp)):
        huancun.append(int(inp[i]))
        huancun.sort()
    arr.append(huancun)
# print(arr)
arr_new = sorted(arr,key=lambda x:x[1])
# print(arr_new)

num = 1
tmp = arr_new[0]
for i in range(1,N):
    if arr_new[i][0] >= tmp[1]:
        num += 1
        tmp = arr_new[i]
print(num)




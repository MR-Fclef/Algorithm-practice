import sys

inp = sys.stdin.readline().split(' ')
n = int(inp[0])
data = []
for i in range(1,n+1):
    data.append(int(inp[i]))

#rint(data)
reward = [1]*n
#print(reward)
for i in range(1,n):
    if i == n-1:
        if data[i]>data[i-1]:
            reward[i] = reward[i-1]+1
        break
    if data[i]>data[i-1] and data[i]<data[i+1]:
        reward[i]=reward[i-1]+1
    if data[i]<data[i-1] and data[i]>data[i+1]:
        reward[i]=reward[i+1]+1
    if data[i]>data[i-1] and data[i]>data[i+1]:
        reward[i]=max(reward[i-1]+1,reward[i+1]+1)

print(sum(reward))


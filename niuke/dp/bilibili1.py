import sys


n = int(sys.stdin.readline())
print(n)
sunshi = []
for i in range(n):
    data = []
    m = sys.stdin.readline().split(',')
    for j in range(len(m)):
        data.append(int(m[j]))
    sunshi.append(data)
print(sunshi)

dp = [[0 for i in range(n)]for j in range(n)]
dp[0][0]=sunshi[0][0]
for i in range(1,n):
    dp[0][i] = dp[0][i-1] + sunshi[0][i]
    dp[i][0] = dp[i-1][0] + sunshi[i][0]
print(dp)

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(dp[i-1][j]+sunshi[i][j],dp[i][j-1]+sunshi[i][j])

print(dp[n-1][n-1])



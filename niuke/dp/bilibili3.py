import sys

data = sys.stdin.readline().split(' ')
m = int(data[0])
n = int(data[1])

arr = []
for i in range(m+1):
    data = []
    m = sys.stdin.readline().split(' ')
    if int(m[0])==-1 and int(m[1])==-1:
        break
    for j in range(n):
        data.append(int(m[j]))
    arr.append(data)
print(arr)
# t = m*n
res = []
start = 0
end = n-1
num = 1
while start<end:
    for i in range(start,end+1):
        res.append(arr[start][i])
        num = num + 1
    for i in range(start+1,end+1):
        res.append(arr[i][end])
        num = num + 1
    for i in range(end-1,start-1,-1):
        res.append(arr[end][i])
        num = num + 1
    for i in range(end-1,start,-1):
        res.append(arr[i][start])
        num = num + 1
    start = start + 1
    end = end -1
    if start == end: 
        res.append(arr[start][end])
print(res)
result = str(res[0])
for i in range(1,len(res)):
    result += ','+str(res[i])
print(result)


# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         result = [[0 for i in range(n)] for j in range(n)]
#         start = 0; end = n-1; num = 1; final = n*n
#         if n == 0:return []
#         while start<end:
#             for i in range(start,end+1):
#                 result[start][i] = num
#                 num = num +1
#             for i in range(start+1,end+1):
#                 result[i][end] = num
#                 num = num + 1
#             for i in range(end-1,start-1,-1):
#                 result[end][i] = num
#                 num = num + 1
#             for i in range(end-1,start,-1):
#                 result[i][start] = num
#                 num = num + 1
#             start = start+1
#             end = end-1
        
#         if start == end: result[start][end]=final
#         return result

# test = Solution()
# print(test.generateMatrix(3))

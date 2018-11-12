class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for j in range(n)]
        start = 0; end = n-1; num = 1; final = n*n
        if n == 0:return []
        while start<end:
            for i in range(start,end+1):
                result[start][i] = num
                num = num +1
            for i in range(start+1,end+1):
                result[i][end] = num
                num = num + 1
            for i in range(end-1,start-1,-1):
                result[end][i] = num
                num = num + 1
            for i in range(end-1,start,-1):
                result[i][start] = num
                num = num + 1
            start = start+1
            end = end-1
        
        if start == end: result[start][end]=final
        return result

test = Solution()
print(test.generateMatrix(3))
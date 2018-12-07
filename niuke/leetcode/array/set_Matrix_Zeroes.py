class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        index_row = []
        index_col = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if (matrix[i][j] == 0) & (i not in index_row):
                    index_row.append(i)
                if (matrix[i][j] == 0) & (j not in index_col):
                    index_col.append(j)
        print(index_col,index_row)
        if len(index_col):
            for i in index_row:
                for j in range(0,len(matrix[0])):
                    matrix[i][j] = 0
            for i in index_col:
                for j in range(0,len(matrix)):
                    matrix[j][i] = 0
            return matrix
        else:
            return matrix
if __name__ == '__main__':
    matrix = [[1,2,3],[2,0,4],[3,4,5]]
    # print(matrix[0][:])
    test = Solution()
    print(test.setZeroes(matrix))



class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # r = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        # r[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i==0)&(j>0):
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif (j==0)&(i>0):
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif (i==0)&(j==0):
                    grid[i][j] = grid[i][j]
                else:
                    if grid[i-1][j]<grid[i][j-1]:
                        grid[i][j] = grid[i-1][j] + grid[i][j]
                    else:
                        grid[i][j] = grid[i][j-1] + grid[i][j]
        print(grid)
        return grid[len(grid)-1][len(grid[0])-1]
if __name__ == '__main__':
    gri = [[1,2],[5,6],[1,1]]
    test = Solution()
    print(test.minPathSum(gri))
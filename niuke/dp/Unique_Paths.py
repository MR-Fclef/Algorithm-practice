class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        Li = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if (i==0)&(j==0):
                    if obstacleGrid[i][j] == 1:
                        Li[i][j] = 0
                    else:
                        Li[i][j] = 1
                elif (i==0)&(j>0):
                    if obstacleGrid[i][j] == 1:
                        Li[i][j] = 0
                    else:
                        Li[i][j] = Li[i][j-1]
                elif (i>0)&(j==0):
                    if obstacleGrid[i][j] == 1:
                        Li[i][j] = 0
                    else:
                        Li[i][j] = Li[i-1][j]
                else:
                    if obstacleGrid[i][j] == 1:
                        Li[i][j] = 0
                    else:
                        Li[i][j] = Li[i-1][j] + Li[i][j-1]
        return Li[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
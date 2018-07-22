# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         m = len(matrix)
#         if m == 0:
#             return False
#         n = len(matrix[0])
#         if n == 0:
#             return False
#         for i in range(m):
#             if target <= matrix[i][-1]:
#                 for j in range(n):
#                     if target == matrix[i][j]:
#                         return True
#             else:
#                 continue
#         return False
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        mfirst,mlast = 0,m - 1
        while mfirst < mlast:
            mid = (mfirst + mlast + 1) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                mfirst = mid
            else:
                mlast = mid - 1
        print(mfirst)
        nfirst,nlast = 0,n - 1
        while nfirst <= nlast:
            mid = (nfirst + nlast) // 2
            if matrix[mfirst][mid] == target:
                return True
            if matrix[mfirst][mid] < target:
                nfirst = mid + 1
            else:
                nlast = mid - 1
        return False

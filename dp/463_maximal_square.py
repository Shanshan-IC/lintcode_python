'''
使用动态规划，可以直接在 matrix 数组上修改，matrix[i][j] 表示以 i, j 为右下角的正方形的边的大小

matrix[i][j] = 0 时，此点不能构成正方形，以 i, j 为右下角的正方形的边的大小为 0
matrix[i][j] = 1 时，此点可以构成正方形，以 i, j 为右下角的正方形的边的大小为 min(以 i-1, j 为右下角的正方形的边的大小，以 i, j-1 为右下角的正方形的边的大小，以 i-1, j-1 为右下角的正方形的边的大小)+1
在遍历时同时保存最大边
正方形大小为边的平方
'''

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        m = len(matrix)
        if m <= 0:
            return 0
        n = len(matrix[0])
        if n <= 0:
            return 0
        res = matrix[0][0]
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] > 0 and matrix[i-1][j] > 0 and matrix[i][j-1] > 0 and matrix[i-1][j-1]:
                    matrix[i][j] = min(matrix[i-1][j-1], min(matrix[i-1][j], matrix[i][j-1])) + 1
                    res = max(res, matrix[i][j])
        return res * res

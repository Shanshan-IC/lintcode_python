class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(n):
            matrix[i].reverse()
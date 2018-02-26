class Solution:
    """
    @param: matrix: A lsit of lists of integers
    @return:
    """
    def setZeroes(self, matrix):
        if matrix is None or len(matrix) == 0:
            return
        m, n = len(matrix), len(matrix[0])
        lm = [0 for _ in range(m)]
        ln = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    lm[i], ln[j] = 1, 1
        for i in range(m):
            for j in range(n):
                if lm[i] == 1 or ln[j] == 1:
                    matrix[i][j] = 0
        return 
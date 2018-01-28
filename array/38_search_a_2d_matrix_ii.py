class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        cnt = 0
        if not matrix or not matrix[0]:
            return cnt
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            val = matrix[r][c]
            if val == target:
                cnt += 1
                c -= 1
            elif val > target:
                c -= 1
            else:
                r += 1
        return cnt

class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = l + (r - l) / 2
            val = matrix[mid/m][mid%m]
            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

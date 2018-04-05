class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if A is None or len(A) == 0:
            return [-1, -1]
        l, r, m = 0, len(A) - 1, 0
        while l + 1 < r:
            m = l + (r - l) / 2
            if A[m] < target:
                l = m
            else:
                r = m
        if A[l] == target:
            l = l
        elif A[r] == target:
            l = r
        else:
            return [-1, -1]
        left, r = l, len(A) - 1
        while l + 1 < r:
            m = l + (r - l) /2
            if A[m] <= target:
                l = m
            else:
                r = m
        if A[r] == target:
            return [left, r]
        else:
            return [left, l]


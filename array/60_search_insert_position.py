class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if A is None or len(A) == 0:
            return 0
        l, r = 0, len(A)-1
        while l + 1 < r:
            m = (l + r)/ 2
            if A[m] == target:
                return m
            elif A[m] < target:
                l = m
            else:
                r = m
        if A[l] >= target:
            return l
        if A[r] >= target:
            return r
        return len(A)
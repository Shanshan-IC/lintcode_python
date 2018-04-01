class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if A is None or len(A) == 0:
            return False
        l, r = 0, len(A) - 1
        while l < r:
            m = l + (r-l)/2
            print(l, r, m)
            if A[m] == target:
                return True
            if (A[m] >= A[l] and target < A[m] and target >= A[l]) or (A[m] <= A[l] and not (target > A[m] and target <= A[r])):
                r = m
            else:
                l = m
        return A[l] == target or A[m] == target

Solution().search([2,2,2,3,1], 1)
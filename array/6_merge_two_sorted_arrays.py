class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        res = []
        i, j = 0, 0
        la, lb = len(A), len(B)
        while (i < la and j < lb):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        while i < la:
            res.append(A[i])
            i += 1
        while j < lb:
            res.append(B[j])
            j += 1
        return res        
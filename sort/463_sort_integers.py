class Solution:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        for i in range(len(A)):
            slices = A[i:]
            idx = slices.index(min(slices))
            A[i], A[idx + i] = A[idx + i], A[i]

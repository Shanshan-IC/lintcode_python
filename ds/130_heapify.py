class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        if A is None or len(A) == 0:
            return A
        n = len(A)
        for i in range(n / 2 - 1, -1, -1):
            self.helper(A, i, n)

    def helper(self, A, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        minN = i
        if left < n and A[left] < A[minN]:
            minN = left
        if right < n and A[right] < A[minN]:
            minN = right
        if minN != i:
            A[i], A[minN] = A[minN], A[i]
            self.helper(A, minN, n)
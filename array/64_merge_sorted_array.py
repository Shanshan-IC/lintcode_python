class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        s = m + n - 1
        a, b = m - 1, n - 1
        while (a >= 0 or b >= 0):
            if a < 0:
                A[s] = B[b]
                b -= 1
            elif b < 0:
                A[s] = A[a]
                a -= 1
            else:
                if A[a] > B[b]:
                    A[s] = A[a]
                    a -= 1
                else:
                    A[s] = B[b]
                    b -= 1
            s -= 1


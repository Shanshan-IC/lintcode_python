class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        a, b = 0, 0
        for num in A:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b
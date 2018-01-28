class Solution:
    """
    @param: A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        both = 0
        for a in A:
            both ^= a
        ans = [0, 0]
        flag = both & (-both)
        for a in A:
            if (a & flag) != 0:
                ans[0] ^= a
            else:
                ans[1] ^= a
        return ans
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False
        d = {i: 0 for i in range(256)}
        for a in A:
            d[ord(a)] += 1
        for b in B:
            if d[ord(b)] == 0:
                return False
            d[ord(b)] -= 1
        return True

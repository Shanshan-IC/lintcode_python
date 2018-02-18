class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        dict_a = {k: 0 for k in range(1, 27)}
        for a in A:
            dict_a[ord(a) % 32] += 1
        for b in B:
            if dict_a[ord(b) % 32] == 0:
                return False
            dict_a[ord(b) % 32] -= 1
        return True


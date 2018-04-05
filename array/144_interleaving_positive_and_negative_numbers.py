class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        if len(A) <= 1:
            return A
        n = len(A)
        pos, neg = [], []
        for a in A:
            if a > 0:
                pos.append(a)
            else:
                neg.append(a)
        if len(pos) > len(neg):
            self.helper(A, pos, neg)
        else:
            self.helper(A, neg, pos)
        return A

    def helper(self, A, pos, neg):
        for i in xrange(len(pos)):
            A[2 * i] = pos[i]
            if i < len(neg):
                A[2 * i + 1] = neg[i]
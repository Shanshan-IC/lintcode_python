class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """
    def cosineSimilarity(self, A, B):
        m, n = len(A), len(B)
        if m != n:
            return 0
        AB, A2, B2 = 0L, 0L, 0L
        for i in xrange(m):
            AB += A[i] * B[i]
            A2 += A[i] * A[i]
            B2 += B[i] * B[i]
        if A2 != 0 and B2 != 0:
            return AB / (math.sqrt(A2) * math.sqrt(B2))
        else:
            return 2.0

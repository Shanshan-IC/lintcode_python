class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        rec = [1]
        idx2, idx3, idx5 = 0, 0, 0
        m2, m3, m5 = rec[idx2] * 2, rec[idx3] * 3, rec[idx5] * 5
        while len(rec) < n:
            while m2 <= rec[-1]:
                idx2 += 1
                m2 = rec[idx2] * 2
            while m3 <= rec[-1]:
                idx3 += 1
                m3 = rec[idx3] * 3
            while m5 <= rec[-1]:
                idx5 += 1
                m5 = rec[idx5] * 5
            rec.append(min(m2, m3, m5))
        return rec[-1]
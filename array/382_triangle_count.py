'''
分析：枚举3条边的话会超时，所以只能枚举最大边和最小边，剩下一条用二分查找来确定范围。
'''

class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        S.sort()
        res, l = 0, len(S)
        for i in xrange(l-2):
            for j in xrange(i+1, l-1):
                k, r = j + 1, l - 1
                target = S[j] + S[i]
                while k <= r:
                    m = k + (r-k)/2
                    if S[m] < target:
                        k = m + 1
                    else:
                        r = m - 1
                res += (k-j-1)
        return res
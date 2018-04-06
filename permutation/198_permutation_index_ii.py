'''
在 lintcode-197-排列序号 的基础上，使用哈希表保存元素出现的次数，对于重复元素 A[i]，A[i] 在 [0,i] 区间中有重复元素，则用 A[i] 的 count * fact 的结果除以重复次数 dup 的阶乘。
'''

class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        res, factor, div = 1, 1, 1
        counter = {}
        for i in xrange(len(A)-1, -1, -1):
            if A[i] not in counter:
                counter[A[i]] = 0
            counter[A[i]] += 1
            div *= counter[A[i]]
            rank = 0
            for j in xrange(i+1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            res += factor * rank / div
            factor *= len(A)-i
        return res

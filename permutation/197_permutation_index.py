'''
首先观察一个全排列， 例如：95412 = X

题目转换成按照字典序，这个全排列之前有多少个全排列。
X的前面的所有全排列中，对于位置1上可以是5, 4, 1, 2任意一个数，而且对应的全排列的基数都是4!个。
同理位置2, 3, 4, 5对应的基数分别是，3！，2！，1！，0！(0!==0)。
得到该位置对应的基数后，那么该位置对应多少个可变数字？9所在位置对应的可变数字的个数为4，分别是5,4,1,2；5所在位置对应的可变数字是4,1,2；4所在位置对应的可变数字是1,2,；1所在位置的对应的可变数字:无。2所在位置对应可变数也是无。
可以得到结论，X全排列某个位置上对应的可变数字的个数 == 这个数后面有多少个比它小的数的个数。
为了得到某个数后面有多少个比它小的数的个数，我们采用折半插入排序（从后向前插入）。
首先计算每一位 A[i] 的后面小于它的数的个数 count，而 i 后面又应该有 n-i-1 位，就有 (n-1-i)! 种排列的可能，所以在 A[i] 之前的可能排列就有 count * (n-1-i)! 个。
所以遍历数组，所有元素的 count * (n-1-i)! 之和再加 1 就是当前排列的序号
'''

class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        res, factor = 1, 1
        for i in xrange(len(A)-1, -1, -1):
            rank = 0
            for j in xrange(i+1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            res += factor * rank
            factor *= len(A)-i
        return res
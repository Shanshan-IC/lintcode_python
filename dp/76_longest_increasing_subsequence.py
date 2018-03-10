'''
开一个栈，每次取栈顶元素top和读到的元素temp做比较，如果temp > top 则将temp入栈；如果temp < top则二分查找栈中的比temp大的第1个数，并用temp替换它。 最长序列长度即为栈的大小top。
这也是很好理解的，对于x和y，如果x < y且Stack[y] < Stack[x],用Stack[x]替换Stack[y]，此时的最长序列长度没有改变但序列Q的''潜力''增大了。

举例：原序列为1，5，8，3，6，7
栈为1，5，8，此时读到3，用3替换5，得到1，3，8； 再读6，用6替换8，得到1，3，6；再读7，得到最终栈为1，3，6，7。最长递增子序列为长度4。

当出现1，5，8，2这种情况时，栈内最后的数是1，2，8不是正确的序列啊？难道错了？
分析一下，我们可以看出，虽然有些时候这样得不到正确的序列了，但最后算出来的个数是没错的，为什么呢？
想想，当temp>top时，总个数直接加1，这肯定没错;但当temp<top时呢？ 这时temp肯定只是替换了栈里面的某一个元素，所以大小不变，就是说一个小于栈顶的元素加入时，总个数不变。这两种情况的分析可以看出，如果只求个数的话，这个算法比较高效。但如果要求打印出序列时，就只能用DP了。
'''

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        q = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > q[-1]:
                q.append(nums[i])
            else:
                l, r = 0, len(q)-1
                while l <= r:
                    m = l+(r-l)/2
                    if nums[i] > q[m]:
                        l = m + 1
                    else:
                        r = m - 1
                q[l] = nums[i]
        return len(q)

'''
dp[i] 表示到i的最长上升子序列
'''

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        for cur, val in enumerate(nums):
            for prev in range(cur):
                if nums[prev] < val:
                    dp[cur] = max(dp[cur], dp[prev] + 1)
        return max(dp)
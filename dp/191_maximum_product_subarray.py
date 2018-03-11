'''
在第 i 位中，乘积最大的连续子序列要么是第 i 位数字本身，要么是前 i-1 位的乘积最大的连续子序列与第 i 位的积
只需一次遍历，在遍历时寻找从第 0 位到第 i 位乘积的最大值，但因为会存在负数（负负得正），所以要同时寻找最小乘积，新的数也要乘以最小乘积在进行比较
dp[i] = max(nums[i], dp[i-1]*nums[i], mins*)
'''
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        mins = [nums[0]]
        maxs = [nums[0]]
        for i in xrange(1, len(nums)):
            maxs.append(max([maxs[i-1] * nums[i], nums[i], mins[i-1] * nums[i]]))
            mins.append(min([maxs[i-1] * nums[i], nums[i], mins[i-1] * nums[i]]))
        return max(maxs)
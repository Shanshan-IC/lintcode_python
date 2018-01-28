class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum = 0
        hs = {0: -1}
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum in hs:
                return [hs[sum]+1, i]
            hs[sum] = i
        return

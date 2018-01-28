# åæ¾å°å¼å§åæ¢çä½ç½®
# è¯¥ä½ç½®å·¦è¾¹ç¿»è½¬ï¼åè¾¹ç¿»è½¬ï¼æåæ´ä½ç¿»è½¬

class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums[0] < nums[-1]:
            return
        pos = 0
        l = len(nums)
        for i in xrange(0, l - 1):
            if nums[i] > nums[i + 1]:
                pos = i
                break
        self.reverse(nums, 0, pos)
        self.reverse(nums, pos + 1, l - 1)
        self.reverse(nums, 0, l - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
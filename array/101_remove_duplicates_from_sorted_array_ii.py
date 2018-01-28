class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if nums == []:
            return 0
        idx = 0
        for i in xrange(1, len(nums)):
            if (nums[idx] != nums[i]) or (idx == 0) or (idx > 0 and nums[idx-1] != nums[idx]):
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
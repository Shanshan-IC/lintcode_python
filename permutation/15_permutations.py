class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums or nums == []:
            return [nums]
        res = []
        self.help(res, [], sorted(nums))
        return res

    def help(self, res, tmp, nums):
        if nums == []:
            res += [tmp]
        else:
            for i in range(len(nums)):
                self.help(res, tmp + [nums[i]], nums[:i] + nums[i + 1:])

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
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
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.help(res, tmp + [nums[i]], nums[:i] + nums[i + 1:])

class Solution:
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        self.res = []
        self.help(sorted(nums), [], 0)
        return self.res

    def help(self, nums, s, idx):
        if idx == len(nums):
            self.res.append(s)
            return
        self.help(nums, s + [nums[idx]], idx + 1)
        self.help(nums, s, idx + 1)
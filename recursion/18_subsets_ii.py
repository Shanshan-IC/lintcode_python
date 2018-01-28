class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        nums.sort()
        p = [[nums[x] for x in range(len(nums)) if i>>x&1] for i in range(2**len(nums))]
        func = lambda x,y:x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))
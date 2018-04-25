class Solution:
    """
    @param nums: n non-negative integer array
    @return: A string
    """

    def minNumber(self, nums):
        # nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: self.cmp(x, y))
        res = ''.join([str(x) for x in nums])
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        return res[i:] if i != len(res) else '0'

    def cmp(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return -1
        elif str(a) + str(b) == str(b) + str(a):
            return 1
        else:
            return 0

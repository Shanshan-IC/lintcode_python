class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        l = len(nums)
        if l <= 1:
            return 0
        res, cnt1, cnt2 = 0, 0, 0
        i = 0
        while i < l and nums[i] == 1:
            i += 1
        while i < l:
            while i < l and nums[i] == 0:
                cnt1 += 1
                i += 1
            while i < l and nums[i] == 1:
                cnt2 += 1
                i += 1
            if cnt1 <= cnt2:
                res += cnt1
                cnt1, cnt2 = 0, 0
        res += min(cnt1, cnt2)
        return res

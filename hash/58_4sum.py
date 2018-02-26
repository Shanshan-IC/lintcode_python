class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        nums.sort()
        l = len(nums)
        res = []
        for i in range(0, l - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, l - 2):
                if j != i + 1 and nums[j] == nums[j-1]:
                    continue
                sum = target - nums[i] - nums[j]
                ll, r = j+1, l-1
                while ll < r:
                    if nums[ll] + nums[r] == sum:
                        res.append([nums[i], nums[j], nums[ll], nums[r]])
                        ll += 1
                        r -= 1
                        while ll < r and ll > 1 and nums[ll] == nums[ll-1]:
                            ll += 1
                        while ll < r and r + 1 < l and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[ll] + nums[r] < sum:
                        ll += 1
                    else:
                        r -= 1
        return res
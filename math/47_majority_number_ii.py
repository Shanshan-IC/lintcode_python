class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        n1, n2, c1, c2 = None, None, 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 += 1
            elif c2 == 0:
                n2 = num
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        return n1 if c1 > c2 else n2
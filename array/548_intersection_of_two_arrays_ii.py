class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        d = {}
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        res = []
        for num in nums2:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        return res
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The majority number
    """

    def majorityNumber(self, nums, k):
        ns = [None for i in xrange(k)]
        cs = [0 for i in xrange(k)]
        for num in nums:
            if num in ns:
                cs[ns.index(num)] += 1
            elif 0 in cs:
                idx = cs.index(0)
                ns[idx] = num
                cs[idx] += 1
            else:
                cs = [i - 1 for i in cs]
        cs = [0 for i in xrange(k)]
        for num in nums:
            if num in ns:
                cs[ns.index(num)] += 1
        return ns[cs.index(max(cs))]

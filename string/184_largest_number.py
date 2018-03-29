class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, num):
        nums = sorted(num, cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
        res = ''.join([str(x) for x in nums])
        i, l = 0, len(res)
        while i + 1 < l:
            if res[i] != '0':
                break;
            i += 1
        return res[i:]


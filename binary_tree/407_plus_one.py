class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        curry = 1
        for i in xrange(len(digits)-1, -1, -1):
            sums = digits[i] + curry
            digits[i] = sums % 10
            curry = sums / 10
        if curry == 1:
            digits.insert(0, 1)
        return digits
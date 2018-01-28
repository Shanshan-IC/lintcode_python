class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        l = len(numbers)
        if l < 3:
            return res
        numbers.sort()
        for i in xrange(l):
            target = 0 - numbers[i]
            # 2 sum
            left, right = i + 1, l - 1
            while left < right:
                if numbers[left] + numbers[right] == target:
                    r = [numbers[i], numbers[left], numbers[right]]
                    if r not in res:
                        res.append(r)
                    left += 1
                    right -= 1
                elif numbers[left] + numbers[right] < target:
                    left += 1
                else:
                    right -= 1
        return res    
class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        l = len(numbers)
        diff = 2 ** 31 - 1
        numbers.sort()
        for i in xrange(l):
            if i - 1 > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, l - 1
            while left < right:
                if left - 1 > i and numbers[left] == numbers[left - 1]:
                    left += 1
                    continue
                s = numbers[left] + numbers[right] + numbers[i]
                if s == target:
                    return target
                elif s < target:
                    if abs(s - target) < diff:
                        diff = abs(s - target)
                        res = s
                    left += 1
                else:
                    if abs(s - target) < diff:
                        diff = abs(s - target)
                        res = s
                    right -= 1
        return res

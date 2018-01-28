class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hash = {}
        for i in xrange(len(numbers)):
            tmp = target - numbers[i]
            if tmp in hash:
                return [hash[tmp], i]
            hash[numbers[i]] = i
        return []
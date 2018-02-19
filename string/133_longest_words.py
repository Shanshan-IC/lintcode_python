class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        l = [len(x) for x in dictionary]
        maxs = max(l)
        return [x for x in dictionary if len(x) == maxs]
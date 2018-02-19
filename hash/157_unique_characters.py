class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        d = {}
        for s in str:
            if s in d:
                return False
            d[s] = 1
        return True
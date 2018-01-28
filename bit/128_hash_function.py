class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        if not key or len(key) == 0:
            return -1
        res = 0
        for a in key:
            res = res * 33 + ord(a)
            res %= HASH_SIZE
        return res


class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        n = len(s)
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, lis):
        if len(s) == 0:
            self.res.append(lis)
            return
        for i in xrange(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], lis + [s[:i]])

    def isPalindrome(self, s):
        for i in xrange(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
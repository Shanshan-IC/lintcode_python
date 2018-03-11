class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        s = str(num)
        l = len(s)
        for i in xrange(0, l/2+1):
            if s[i] != s[l-i-1]:
                return False
        return True

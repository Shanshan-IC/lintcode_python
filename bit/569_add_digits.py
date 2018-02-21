"""
438  == 40*10 +3*10 +8 ;
4+3+8 == 4*(10%9)*(10%9)+3*(10%9)+8%9= 15   ;
15  == 1*10 + 5 ;
1+5 == 1*(10%9)+5%9= 6 ;
"""
class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9

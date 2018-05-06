'''
这道题给了我们一个数字，让我们进行因数分解，让我们找出因数组成的最小的数字。从题目中的例子可以看出，分解出的因数一定是个位数字，即范围是[2, 9]。那我们就可以从大到小开始找因数，首先查找9是否是因数，是要能整除a，就是其因数，如果是的话，就加入到结果res的开头，a自除以9，我们用while循环查找9，直到取出所有的9，然后取8，7，6...以此类推，如果a能成功的被分解的话，最后a的值应该为1，如果a值大于1，说明无法被分解，返回true。最后还要看我们结果res字符转为整型是否越界，越界的话还是返回0
'''

class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        res, base = 0, 1
        for i in xrange(9, 1, -1):
            while a % i == 0:
                a /= i
                res += i * base
                if res > 2147483647:
                    return 0
                base *= 10
        return res if a == 1 else 0
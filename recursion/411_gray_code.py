'''
在实现的时候，我们完全可以利用递归，在每一层前面加上0或者1，然后就可以列出所有的格雷码。
比如：

第一步：产生 0, 1 两个字符串。
第二步：在第一步的基础上，每一个字符串都加上0和1，但是每次只能加一个，所以得做两次。这样就变成了 00,01,11,10（注意对称）。
第三步：在第二步的基础上，再给每个字符串都加上0和1，同样，每次只能加一个，这样就变成了000,001,011,010,110,111,101,100。
好了，这样就把3位元格雷码生成好了。
如果要生成4位元格雷码，我们只需要在3位元格雷码上再加一层0,1就可以了：0000,0001,0011,0010,0110,0111,0101,0100,1100,1101,1110,1010,0111,1001,1000.
也就是说，n位元格雷码是基于n-1位元格雷码产生的。
'''


class Solution:
    """
    @param n: a number
    @return: Gray code
    """

    def grayCode(self, n):
        if n == 0:
            return [0]
        res = self.grayCode(n - 1)
        seq = list(res)
        for i in reversed(res):
            seq.append((1 << (n - 1)) | i)
        return seq


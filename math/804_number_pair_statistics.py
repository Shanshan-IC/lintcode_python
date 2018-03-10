class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """

    def pairNumbers(self, p):
        size = len(p)
        if size <= 1:
            return 0
        rec = [[0, 0] for _ in range(size)]
        for i in xrange(size):
            if p[i][0] & 1:
                rec[i][0] = 1
            if p[i][1] & 1:
                rec[i][1] = 1
        res = 0
        for i in range(size - 1):
            for j in range(i + 1, size):
                if rec[i][0] == rec[j][0] and rec[i][1] == rec[j][1]:
                    res += 1
        print(res)
        return res

Solution().pairNumbers([[0,3],[1,1],[3,4],[5,6]])
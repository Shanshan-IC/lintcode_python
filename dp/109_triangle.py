'''
dp[i][j]表示从第i行第j列到达底部的最短路径
dp[i][j] = triangle[i][j] + min(dp[i][j+1], dp[i+1][j+1])
'''
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return 0
        tmp = triangle[-1] # 最后一行
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                tmp[j] = triangle[i][j] + min(tmp[j+1], tmp[j])
        return tmp[0]

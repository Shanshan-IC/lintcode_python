# method 1 贪心算法

class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        maxs = 0
        for i in range(len(A)):
            if i > maxs:
                return False
            maxs = max(maxs, i + A[i])
        return True

# method 2 动态规划
# dp[i] 表示位置i能够跳跃的最大长度
# dp[i] = max(dp[i-1], A[i]+i) if dp[i-1] >= i

class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if A is None or len(A) == 0:
            return True
        dp = [A[0]]
        for i in range(1, len(A)):
            if dp[i-1] >= i:
                dp.append(max(dp[i-1], A[i]+i))
            else:
                dp.append(0)
        return dp[-1] >= len(A)-1
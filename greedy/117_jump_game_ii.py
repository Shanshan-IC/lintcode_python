'''
使用贪心算法，用2个变量 end, farthest 分别从当前（第 i 位）到第 end 位，可以一次跳跃的最远距离farthest ，当移动到第 end 位时，再次跳跃，直至跳出
'''
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if A is None or len(A) == 0:
            return 0
        end, farthest, mins = 0, 0, 0
        for i in range(len(A)):
            farthest = max(farthest, A[i] + i)
            if i == end and end < len(A)-1:
                mins += 1
                end = farthest
        return mins
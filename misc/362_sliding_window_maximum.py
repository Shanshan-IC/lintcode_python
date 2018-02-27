from collections import deque

class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, nums, k):
        if nums is None or len(nums) == 0:
            return nums
        if len(nums) < k or k == 0:
            return []
        q = deque()
        res = []
        for i in range(len(nums)):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i < k - 1:
                continue
            while len(q) and q[0] <= i - k:
                q.popleft()
            res.append(nums[q[0]])
        return res
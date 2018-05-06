class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """

    def reverseStore(self, head):
        self.res = []
        self.dfs(head)
        return self.res

    def dfs(self, head):
        if head is None:
            return
        self.dfs(head.next)
        self.res.append(head.val)
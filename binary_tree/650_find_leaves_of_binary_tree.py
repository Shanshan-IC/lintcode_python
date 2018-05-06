'''
这道题换句话说就是找每个node的index，这个index就是最后结果中这个节点所在的list的index，比如4,5,3的index是0， 2的index是1，1的index是2.
怎么找呢？二分，看左，看右。
确定一个点的index，得知道他的左孩子index是多少，右孩子的index是多少，当前这个点的index是他左右孩子的index最大值+1，这可以很容易地观察得到。比如对于1来说，左孩子2的index是1，右孩子3的index是0，那1的index肯定是max(1, 0) + 1，即2.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """

    def findLeaves(self, root):
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return -1
        left = self.helper(root.left)
        right = self.helper(root.right)
        cur = max(left, right) + 1
        if len(self.res) == cur:
            self.res.append([])
        self.res[cur].append(root.val)
        return cur
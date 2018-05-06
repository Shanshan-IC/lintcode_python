"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

'''
假如前序遍历是 {1,2,4,5,6,3,7,8}，中序遍历是 {4,2,6,5,1,3,8,7}，前序遍历中的第一个值就是根节点，这个节点把中序遍历分成了两部分，分别对应根节点的左右子树，则左子树的中序遍历是左边部分 (4,2,6,5)，一共4个数字，所以左子树的前序遍历是根节点 1 之后的 4 个数字 (2,4,5,6)。于是进入递归分析左子树，左子树分析完之后用同样的方式分析右子树即可。


'''


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, preorder, inorder):
        if preorder is None or len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        idx = self.getIndex(inorder, preorder[0])
        if len(preorder) == 1:
            return node
        if idx > 0:
            node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        if idx < len(inorder) - 1:
            node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node

    def getIndex(self, node, key):
        for i in xrange(len(node)):
            if key == node[i]:
                return i
        return -1
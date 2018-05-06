"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if nestedList is None or len(nestedList) == 0:
            return 0
        st = [(n, 1) for n in nestedList]
        res = 0
        while st:
            next, d = st.pop(0)
            if next.isInteger():
                res += d * next.getInteger()
            else:
                for i in next.getList():
                    st.append((i, d+1))
        return res

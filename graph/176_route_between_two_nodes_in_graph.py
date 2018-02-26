"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        record = {}
        for x in graph:
            record[x] = 0
        return self.dfs(graph, record, s, t)

    def dfs(self, graph, record, s, t):
        if s in record and record[s] == 1:
            return False
        if s == t:
            return True
        record[s] = 1
        for i in s.neighbors:
            if record[i] == 0 and self.dfs(graph, record, i, t):
                return True
        return False

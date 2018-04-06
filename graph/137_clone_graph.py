"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

import collections
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        root = node
        if node is None:
            return None
        nodes = self.getNodes(node)
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        return mapping[root]

    def getNodes(self, node):
        q = collections.deque([node])
        res = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in res:
                    q.append(neighbor)
                    res.add(neighbor)
        return res
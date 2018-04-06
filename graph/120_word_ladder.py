'''
可以将此题理解为求图中两点的最短路径，dict 中每个单词是一个节点，start 与 end 也是图中的节点，若两个单词中只有一个字母不同（如 "hit" "hot" "dog"）在，则这两个节点是联通的。故问题就转化成了在图中求节点 start 到节点 end 的最短路径。
网上普遍的解法，在遍历节点的相邻节点处做了优化，在得到队列头结点时，枚举所有与头结点相连的节点值，并判断此值是否在图中（即 dict 中）。若此节点未被遍历过（即此节点存在于 dict），将其加入队列并更新距离，然后将此节点删除（减少搜索代价），否则，继续枚举


'''

import collections

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        size = len(start)
        q = collections.deque([(start, 1)])
        while q:
            cur = q.popleft()
            cur_word = cur[0]
            cur_size = cur[1]
            if cur_word == end:
                return cur_size
            for i in xrange(size):
                p1 = cur_word[:i]
                p2 = cur_word[i+1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if cur_word[i] != j:
                        new_word = p1 + j + p2
                        if new_word in dict:
                            q.append((new_word, cur_size+1))
                            dict.remove(new_word)
        return 0
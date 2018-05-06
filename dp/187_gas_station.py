class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0:
            return 0
        l = len(gas)
        # start: 从第start个加油站开始走
        # cur：当前的存储量
        # gas：当前汽油总量
        # cost：走完环路的消耗总量
        start, cur, g, c = 0, 0, 0, 0
        for i in xrange(l):
            cur += gas[i]
            cur -= cost[i]
            g += gas[i]
            c += cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if g >= c else -1
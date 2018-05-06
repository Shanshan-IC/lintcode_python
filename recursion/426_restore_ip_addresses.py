'''
使用递归+回溯，需要注意的是合法 ip 的判断，即：

每一节的数组均在 0 到 255 之间，包含 0 和 255
001，01 均是不合法的，但 0 ，10，100合法
共有4节，不多不少
'''


class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        ips = []
        self.dfs(s, 0, ips, '')
        return ips

    def dfs(self, s, sub, ips, ip):
        if sub == 4:
            if s == '':
                ips.append(ip[1:])
                return
        for i in xrange(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                if s[0] == '0':
                    break
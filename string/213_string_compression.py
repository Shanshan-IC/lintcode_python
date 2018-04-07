class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, ss):
        if len(ss) == 0:
            return ""
        s, i, cnt = ss[0], 0, 1
        res = ""
        while i < len(ss):
            while i < len(ss)-1 and ss[i+1] == s:
                cnt += 1
                i += 1
            res = res + s + str(cnt)
            if i+1 >= len(ss):
                break
            s = ss[i+1]
            cnt = 1
            i += 1
        return res if len(res) < len(ss) else ss
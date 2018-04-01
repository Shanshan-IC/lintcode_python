'''
采用哈希映射记录字符串中每个字母出现的次数，字符ASCII码有128个，所以用大小为128位的数组记录字符串中每个字母出现的次数，如countSource['A']表示A出现的次数，而不是用countSource[0]表示。

先用countTarget数组记录target中每个字符出现的次数，用begin,end记录最小子串覆盖（MVS）在source中的起始位置和结束位置，之后遍历source。
'''
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        if source == "" or target == "":
            return ""
        d, dt = {}, dict.fromkeys(target, 0)
        for c in target: d[c] = d.get(c, 0) + 1
        i, j, cnt = 0, 0, 0
        ans = ""
        while j < len(source):
            if source[j] in dt:
                if dt[source[j]] < d[source[j]]:
                    cnt += 1
                dt[source[j]] += 1
            if cnt == len(target):
                while i < j:
                    if source[i] in dt:
                        if dt[source[i]] == d[source[i]]:
                            break
                        dt[source[i]] -= 1
                    i += 1
                if ans == '' or j - i < len(ans):
                    ans = source[i:j+1]
                dt[source[i]] -= 1
                i += 1
                cnt -= 1
            j += 1
        return ans
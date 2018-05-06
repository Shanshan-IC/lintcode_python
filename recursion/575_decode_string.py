class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        st = []
        cnt = 0
        for c in s:
            if c.isdigit():
                cnt = cnt * 10 + int(c)
            elif c == '[':
                st.append(str(cnt))
                cnt = 0
            elif c == ']':
                tmp = self.helper(st)
                times = int(st.pop())
                ss = ''
                for i in xrange(times):
                    ss += tmp
                st.append(ss)
            else:
                st.append(c)
        return self.helper(st)

    def helper(self, st):
        tmp = ''
        while st:
            if st[-1].isdigit():
                break
            tmp = st.pop() + tmp
        return tmp
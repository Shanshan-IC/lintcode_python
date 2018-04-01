class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        if s is None or len(s) == 0:
            return True
        st = []
        for ss in s:
            if ss == '(' or ss == '[' or ss == '{':
                st.append(ss)
            else:
                if len(st) == 0:
                    return False
                if ss == ']' and st[-1] != '[' or ss == '}' and st[-1] != '{' or ss == ')' and st[-1] != '(':
                    return False
                st.pop()
        return len(st) == 0


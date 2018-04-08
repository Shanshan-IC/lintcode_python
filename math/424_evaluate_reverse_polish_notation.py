class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        st = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                st.append(int(t))
            else:
                a = st.pop()
                b = st.pop()
                if t == '+': st.append(a+b)
                elif t == '-': st.append(b-a)
                elif t == '*': st.append(a*b)
                else: st.append(int(b*1.0/a))
        return st[0]
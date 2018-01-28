class MinStack:
    def __init__(self):
        self.st = []
        self.min_st = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.st.append(number)
        if self.min_st == [] or self.min_st[-1] >= number:
            self.min_st.append(number)

    """
    @return: An integer
    """

    def pop(self):
        if self.min_st[-1] == self.st[-1]:
            self.min_st.pop()
        return self.st.pop()

    """
    @return: An integer
    """

    def min(self):
        return self.min_st[-1]


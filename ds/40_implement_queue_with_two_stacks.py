class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.s1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        self.helper()
        return self.s2.pop()

    """
    @return: An integer
    """

    def top(self):
        self.helper()
        return self.s2[len(self.s2) - 1]

    def helper(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())

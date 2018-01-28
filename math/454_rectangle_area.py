class Rectangle:
    '''
     * Define a constructor which expects two parameters width and height here.
    '''

    def __init__(self, x, y):
        self.width = x
        self.height = y

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''

    # write your code here
    def getArea(self):
        return self.width * self.height
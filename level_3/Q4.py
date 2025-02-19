class Shape():

    def __init__(self):
        self._area = 0

    def area(self):
        return self._area


class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.side = length

    def area(self):
        self._area = self.side * self.side
        return self._area

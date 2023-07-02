class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area_rectangle(self):
        area = self.base * self.height
        return area

    def length_rectangle(self):
        length = 2 * (self.base + self.height)
        return length



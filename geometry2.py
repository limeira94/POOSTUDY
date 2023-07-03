from math import sqrt, pi

class Point:
    def __init__(self, x: float, y: float) -> float:
        self.x = x
        self.y = y

    def distance_origin(self):
        distance = sqrt(self.x**2 + self.y**2)
        return distance

    def distance_between_points(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return sqrt(dx**2 + dy**2)


class Circle:
    def __init__(self, center, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        area_circle = pi * self.radius**2
        return round(area_circle, 0)

    def circumference(self) -> float:
        circf = 2 * pi * self.radius
        return round(circf, 0)

    def point_within(self, other_point):
        distance = self.center.distance_between_points(other_point)
        return distance <= self.radius


def test_distance_origin():
    ponto1 = Point(1, 2)
    ponto2 = Point(3, 4)
    assert ponto1.distance_origin() == sqrt(5)
    assert ponto2.distance_origin() == 5.0

def test_distance_between_points():
    ponto1 = Point(1, 1)
    ponto2 = Point(4, 1)
    ponto3 = Point(3, 1)
    ponto4 = Point(1, 3)
    assert ponto1.distance_between_points(ponto3) == 2.0
    assert ponto2.distance_between_points(ponto4) == sqrt(13)

def test_area_circle():
    ponto1 = Point(0, 0)
    circulo1 = Circle(ponto1, 8)
    assert circulo1.area() == round(200.96, 0)

def test_circumference():
    ponto1 = Point(0, 0)
    circulo1 = Circle(ponto1, 30)
    assert circulo1.circumference() == round(188.4, 0)

def test_point_within():
    ponto = Point(3, 4)
    centro = Point(0, 0)
    circulo = Circle(centro, 5)
    assert circulo.point_within(ponto) is True

def test_point_no_within():
    ponto = Point(3, 4)
    centro = Point(0, 0)
    circulo = Circle(centro, 4)
    assert circulo.point_within(ponto) is False

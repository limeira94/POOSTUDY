class Circle:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia


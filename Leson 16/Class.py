class TriangleChekcr:
    @staticmethod
    def is_triangle(a, b, c):
        if not (isinstance(a,(int , float))and isinstance(b,(int , float))and isinstance(c,(int , float))):
            return "Нужно вводить только числа!"
        elif a <=0 or b <= 0 or c <= 0:
            print("Из отрицательных чисел не получится ")
        elif a + b > c and a + c > b and c + b > a:
            return "Ура, можно постороить треугольник!"
        else:
            return "Ничего не получится("

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class ExtTriangle (Triangle, TriangleChekcr):
    def __init__(self, a, b, c):
        Triangle.__init__(self, a, b, c)

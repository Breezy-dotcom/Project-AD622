from math import pi

circle = lambda r: pi * r**2
rectangle = lambda a, b: a * b
trapezoid = lambda a, b, h: (a + b) * h / 2

print("Площадь окружности радиуса 2:", circle(2))
print("Площадь прямоугольника размером 10*13:", rectangle(10,13))
print("Площадь трапеции для a=7, b=5, h=3:", trapezoid(7, 5, 3))
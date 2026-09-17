def rectangle(base,height):
    return base*height
def triangle(base,height):
     return base*height/2
def circle(radius):
    return 3.14*radius*radius

figure = int(input("1-Rectangle 2-Triangle 3-circle:"))
if figure == 1:
  base = float(input("Base:"))
  height = float(input("Height:"))
  print(rectangle(base,height))

elif figure == 2:
  base = float(input("Base:"))
  height = float(input("Height:"))
  print(triangle(base,height))

elif figure == 3:
  radius = float(input("Radius:"))
  print(circle(radius))





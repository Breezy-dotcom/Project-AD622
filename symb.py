num=int(input("Введите количество символов"))
symb=input("Введите символ:")
print("0-горизонтальная\n1-вертикальная")
line=int(input("Ориентация линии:"))

i=0
if line == 0:
    while i<num:
        print(symb,end=" ")
        i+=1

elif line == 1:
    while i<num:
        print(symb,end=" ")
        i+=1


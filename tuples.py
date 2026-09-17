import random
def creat_tuple(start, end):
    numbers = ()

    for i in range(10):
        num=random.randint(start, end)
        numbers += (num,)
    return numbers

tuple1 = creat_tuple(0,5)
tuple2 = creat_tuple(-5,0)

tuple3 = tuple1 + tuple2
zeros = tuple3.count(0)

print(tuple1)
print(tuple2)
print(tuple3)
print("0=",zeros)









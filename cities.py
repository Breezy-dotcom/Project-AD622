def func(city):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(city, count)

    return inner

res1 = func("Москва")
res2 = func("Сочи")
res1()
res1()
res2()
res2()
res1()




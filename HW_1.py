# 1: Создание Series и фильтрация

import pandas as pd

sales = pd.Series(
    [12, 15, 8, 20, 25, 30, 10],
    index=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
)

print(sales)

filtered_sales = sales[sales > 15]
print(filtered_sales)



# 2: Поиск топ-N значений

import pandas as pd

scores = pd.Series(
    [85, 90, 78, 92, 88, 76, 95, 92],
    index=['Аня', 'Боря', 'Блад', 'Глаша', 'Дима', 'Ева', 'Жора', 'Зина']
)

print(scores)

top_3 = scores.nlargest(3)
print(top_3)



# 3: Проверка условий (True / False)

import pandas as pd

ages = pd.Series([16, 25, 38, 17, 42, 15])
print(ages)

adults = ages >= 18
print(adults)



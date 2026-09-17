sales = {
    "John": {
         "N": 3056,
         "S": 8463,
         "E": 8441,
         "W": 2694

    },

    "Tom": {
         "N": 4832,
         "S": 6786,
         "E": 4737,
         "W": 3612

    },

    "Anne": {
         "N": 5239,
         "S": 4802,
         "E": 5820,
         "W": 1859

    },

    "Fiona": {
         "N": 3904,
         "S": 3645,
         "E": 8821,
         "W": 2451

    },


}

for name in sales:
    print(name)

    for region in sales[name]:
        print(region, ": ", sales[name][region])

name = input("Name: ")
region = input("Region: ")
print(sales[name][region])

new_value = int(input("New value: "))
sales[name][region] = new_value
print(sales[name])



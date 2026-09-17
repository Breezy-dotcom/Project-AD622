math = ["Matvei","Evgeniya","Mikhail","Maxim","Natalia"]
physics = ["Maxim", "Matvei","Alexandr"]

all_winners = set(math + physics)
both = set(math) & set(physics)
math = both

del physics

print("all winners:",all_winners)
print("Winners of both olympiads:",both)
print("updated math list:",math)
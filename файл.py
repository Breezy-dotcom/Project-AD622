pos1 = 1
pos2 = 2

with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines[pos1], lines[pos2] = lines[pos2], lines[pos1]
with open("text.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Результат:")
for line in lines:
    print(line, end="")
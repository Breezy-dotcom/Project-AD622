text = """Ежевижу для ежат
Принесли два ежа.
Ежевижу еле-еле 
Ежата восле ели сьели."""

text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("-", "")

words = text.split()

count = 0
for word in words:
    if word.startswith("е"):
        count += 1

print("Количество слов: ", count)
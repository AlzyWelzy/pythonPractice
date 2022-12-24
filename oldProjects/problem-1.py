sum = 0
# allItems = []

kiranaItems = {
    "sugar": 15,
    "flour": 27,
    "oil": 49,
    "nuts": 180
}

for key, value in kiranaItems.items():
    purchase = int(
        input(f"How much {key} you purchased. Rs. {value} per Kg: "))
    sum += kiranaItems.get(key)*purchase

print(f"Your total bill is: {sum}")

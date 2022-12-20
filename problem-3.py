with open("currencyData.txt", "r") as f:
    lines = f.readlines()

currencyDict = {}

# print(lines)

for line in lines:
    parsed = line.split("\t")
    print(parsed)
    currencyDict[parsed[0]] = parsed[1]

# print(currencyDict)

inr = float(input("Enter the amount you want to convert: "))

# for key, value in currencyDict.items():
#     print(f"INR {inr} converts to {key} {float(value)*inr}.")

print(f"Enter the name of the currency you want to convert this amount to? Available Options: ")

[print(item) for item in currencyDict.keys()]

currency = input("Please enter one of these values: ")

print(f"{inr} INR is equal to {inr*float(currencyDict.get(currency))} {currency}.")

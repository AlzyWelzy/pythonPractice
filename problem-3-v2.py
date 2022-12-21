with open("currencyData.txt") as f:
    lines = f.readlines()

currencyDict = {}

print(lines)

supParsed = []

# with open("extraText.txt") as f:
for line in lines:
    parsed = line.split(" \t")
    print(parsed)
    parsed[2] = parsed[2].replace("\n", "")
    print(parsed)
    # supParsed.append(parsed)
    currencyDict[parsed[0]] = parsed[1]

print(currencyDict)

amount = float(input("Enter the amount in INR to convert: "))

print(
    f"Enter the name of the currency from the following option to convert the amount of {amount} to: ")

[print(item) for item in currencyDict.keys()]

currency = input("Please enter one of these: ")

print(f"{amount} INR is equal to {round(amount*float(currencyDict.get(currency)),4)} {currency}.")

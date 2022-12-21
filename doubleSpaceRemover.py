import itertools
with open("extraText.txt") as f:
    lines = f.readlines()

print(lines)

supParsed = []

# with open("extraText.txt") as f:
for line in lines:
    parsed = line.split(" \t")
    print(parsed)
    parsed[2] = parsed[2].replace("\n", "")
    print(parsed)
    supParsed.append(parsed)

print(supParsed)

# print(supParsed.join("\n"))
# print("\n".join(supParsed))

# result = list(itertools.chain.from_iterable(supParsed))

# print(result)

for data in supParsed:
    with open("newData.txt", "a") as f:
        # print(data, type(data))
        # print('\n'.join(data))
        f.write(" ".join(data))
        f.write("\n")

def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp)
        o.append(row)
    return o


m = int(input("Enter the value for m: "))
n = int(input("Enter the value for n: "))

print("Enter martiix A")
X = matrix(m, n)
print(X)

print("Enter martiix B")
Y = matrix(m, n)
print(Y)

result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)

print(result)

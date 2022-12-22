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
A = matrix(m, n)
print(A)

print("Enter martiix B")
B = matrix(m, n)
print(B)

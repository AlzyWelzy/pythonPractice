def isPalindro(val):
    try:
        isNeg = "+"
        if val.isalnum() or val.isalpha():
            return False

        if '.' in val or " " in val:
            return False

        if int(val) < 0:
            isNeg = "-"

        valSplit = [char for char in val]
        valSplit.reverse()
        valSplit.remove("-")
        valSplit.insert(0, isNeg)
        return int(val) == int("".join(valSplit))
    except Exception as e:
        return e


value = input("Enter a positive value: ")
# print(isPalindro(value))


def isPalindrome(val):

    if not val.isdigit() or '.' in val or " " in val:
        return False

    val = str(val)
    return val == val[::-1]


def isPalindrome(val):
    val = str(val)  # Convert the input to a string
    return val == val[::-1]  # Check if the string is equal to its reverse


print(isPalindrome(value))

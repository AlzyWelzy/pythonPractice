def isArmstrong(val):
    try:
        # Check if val is a number
        if not val.isdigit():
            return False

        # Check if val is a positive integer
        if int(val) < 0 or '.' in val:
            return False

        # Check if val has leading zeros
        if val[0] == '0':
            return False

        # Calculate the sum of the digits of val, each raised to the power of the number of digits in val
        checkVal = 0
        for i in val:
            checkVal = checkVal + (int(i) ** len(val))

        # Check if checkVal is a multiple of val
        return checkVal % int(val) == 0
    except Exception as e:
        return e


value = input("Enter a value: ")
print(isArmstrong(value))

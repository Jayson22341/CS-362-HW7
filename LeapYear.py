def YearCheck(x):
    if x % 4 == 0:
        if x % 100 == 0:
            return False
        return True
    return False

print("This is the Leap-Year-Check program!")
print("Give me a year, and I'll tell if its a leap year or not!")
x = int(input("Enter in a year: "))
boolVar = YearCheck(x)
if boolVar == True:
    print("The year: ", x, " is a leap year!")
elif boolVar == False:
    print("The year: ", x, "is NOT a leap year...")

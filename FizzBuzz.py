

def FizzBuzz(x):
    if x % 3 == 0 or x % 5 == 0:
        returnstring = ""
        if x % 3 == 0:
            returnstring += "Fizz"
        if x % 5 == 0:
            returnstring += "Buzz"
        return returnstring
    return x

print("This is the FizzBuzz Program! I'm gonna do my thing!")
for x in range(1,101):
    print(FizzBuzz(x))

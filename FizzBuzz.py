

def FizzBuzz(x):
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return x

print("This is the FizzBuzz Program! I'm gonna do my thing!")
for x in range(1,101):
    print(FizzBuzz(x))

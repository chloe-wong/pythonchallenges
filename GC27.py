n = 1
while n <= 20:
    if n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    elif n%15 == 0:
        print("FizzBuzz")
    else:
        print(n)
    n = n+1
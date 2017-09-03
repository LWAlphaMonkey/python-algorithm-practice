def fizBuzz(num):
    for x in range(0, num+1):
        if (x % 15 == 0):
            print("Fizz Buzz")
        elif (x % 3 == 0):
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        else:
            print(x)

fizBuzz(20)


def factorial(num):
    if num == 2:
        return 2
    while num > 2:
        return num * factorial(num - 1)

print("f(2): ", factorial(2))
print("f(3): ", factorial(3))
print("f(4): ", factorial(4))
print("f(5): ", factorial(5))
print("f(6): ", factorial(6))
print("f(7): ", factorial(7))

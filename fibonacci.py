import time

def fibonacci(position):
    if position < 3:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)

for i in range(1, 21):
    t0 = time.time()
    print("fibonacci(" , i, ") is ", fibonacci(i))
    t1 = time.time()
    print("total time", t1 - t0)

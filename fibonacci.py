import time


def fib(n):
    if n == 0:
        print("Error : ", end="")
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo):
    if (memo[n] != 0):
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result


def fib_myStyle(n):
    if n == 1 or n == 2:
        return 1
    fib_array = []
    fib_array.append(1)
    fib_array.append(1)
    for i in range(2, n - 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    return fib_array[-1]


# n = int(input("Fibonnaci of : "))
n = 10000

# print("Using simple recursive")
# start = time.time()
# print(fib(n))
# end = time.time()
# print(end - start)


# print("Using memoize")
# start = time.time()
# given_array = []

# for i in range(n+1):
#    given_array.append(0)
#
# print(fib_memo(n, given_array))
# end = time.time()
# print(end - start)

print(f'{n}th Fibonacci no. : ')
start = time.time()
print(f'{fib_myStyle(n)}')
end = time.time()
print(end - start)

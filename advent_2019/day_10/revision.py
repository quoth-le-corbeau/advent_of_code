CACHE = {}


def fib(n):
    if n in CACHE:
        return CACHE[n]
    if n in [1, 2]:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    CACHE[n] = result
    return result


def fib_iter(n):
    if n in [1, 2]:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


print(f"{fib(23)=}")
print(f"{fib(5)=}")
print(f"{fib(3)=}")
print(f"{fib(7)=}")
print(f"{fib(6)=}")
print(f"{fib(2)=}")

print(f"{fib_iter(3333)=}")
# max 1000 recursion depth exceeded:
print(f"{fib(3333)=}")

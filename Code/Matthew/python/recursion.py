





# factorial
# 1! = 1
# 2! = 2*1
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120




# print(list(range(10)))
# print(list(range(1, 11)))


def factorial(n):
    r = 1
    for j in range(n):
        r *= (j+1)
    return r


def factorial2(n):
    r = 1
    while n > 0:
        r *= n
        n -= 1
    return r


def factorial_recursive(n):
    if n == 1:
        print('base case: factorial(1) == 1')
        return 1
    print(f'recurse: {n}*factorial({n-1})')
    r = n*factorial_recursive(n-1)
    print(f'returning {r}')
    return r




# O(n)
def fibonacci(n):
    if n <= 2:
        return 1
    fib = [1, 1]
    for i in range(3, n+1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


# O(1)
def fibonacci_closed(n):
    sqrt5 = 5**(1/2)
    phi = (1 + sqrt5) / 2
    psi = 1 - phi
    return ((phi ** n) - (psi ** n))/sqrt5


# print(round(fibonacci_closed(9)))

# f(n) = f(n-1) + f(n-2)
# 1, 1, 2, 3, 5, 8, 13, 21, 34

global x

x = 0

# O(2^n)
def fibonacci_recursion(n):
    global x
    x += 1
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print(fibonacci(40))

print(x)

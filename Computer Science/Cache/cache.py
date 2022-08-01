import sys
from timeit import Timer
sys.setrecursionlimit(10000)


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)


def memoization_factorial(n):
    global memo
    if n < 2:
        return 1
    if not memo.get(n):
        memo[n] = n * memoization_factorial(n-1)
    return memo[n]


memo = dict()
n = 1000
factorial_time = Timer(f"factorial({n})", "from __main__ import factorial").timeit(number=1000)
memoization_factorial_time = Timer(f"memoization_factorial({n})", "from __main__ import memoization_factorial").timeit(number=1000)

print(f"{n}! 재귀함수 : {factorial_time}s")
print(f"{n}! 캐시함수 : {memoization_factorial_time}s")

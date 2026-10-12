"""
39. Fibonacci (nth number)
fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).

Approach: bottom-up with two rolling variables (no array, no recursion).
Time: O(n)   Space: O(1)

Shortcut: "a, b = 0, 1; loop n times: a, b = b, a + b; return a."
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print(fib(10))   # Output: 55
    print([fib(i) for i in range(8)])   # Output: [0, 1, 1, 2, 3, 5, 8, 13]


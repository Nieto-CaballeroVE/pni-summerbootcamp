"""
Exercise 2 starter code.

A naive recursive Fibonacci function. Run test_fib_starter.py against it
It currently fails, so fix this file (not the test file) until all tests pass.

Reminder of the definition:
    F(0) = 0
    F(1) = 1
    F(x) = F(x-1) + F(x-2) for x > 1
"""


def fib(x):
    if x < 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)

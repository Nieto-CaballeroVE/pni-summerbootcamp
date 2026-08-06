"""
Exercise 2: run `pytest test_fib_starter.py` and fix fib_buggy.py until
everything passes. Don't edit the tests, just edit the implementation.
"""

from pni_bootcamp.fib_buggy import fib


def test_typical():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8


def test_edge_case():
    # Look closely at what fib(0) should return versus what it does return.
    assert fib(0) == 0


def test_larger_value():
    # Correctness check on a bigger input. If this test takes more than a
    # few seconds to run, that's your cue for Part B: add memoization (a
    # cache dict) to fib_buggy.py, then rerun this whole file to confirm
    # you didn't break anything.
    assert fib(40) == 102334155



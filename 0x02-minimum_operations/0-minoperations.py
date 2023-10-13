#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in
exactly n H characters in the file.

- Prototype: def minOperations(n)
- Return an integer
- If n is impossibl to achieve, return 0
"""


 ops = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
            ops += factor
        factor += 1

    if n > 1:
        ops += n
    return ops

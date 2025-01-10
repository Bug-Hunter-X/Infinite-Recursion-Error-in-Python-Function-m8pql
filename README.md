# Infinite Recursion Bug in Python

This repository demonstrates a common error in recursive functions: infinite recursion due to missing base cases.

The `bug.py` file contains a Python function that suffers from this issue. When called with a negative number, it recurses infinitely, leading to a `RecursionError`.  The `bugSolution.py` file shows the corrected function with a proper base case to handle all possible inputs.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py` with a negative integer argument. You should observe a `RecursionError`.
3. Run `bugSolution.py`. This will execute without error.
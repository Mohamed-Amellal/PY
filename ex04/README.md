# Exercise 04 — The Even and the Odd

**File:** `whatis.py` · **Allowed:** `sys` or any lib to receive the args

## Goal
Take one number as a command-line argument and print whether it is odd or even.

## Rules
- **0 arguments** → print nothing (no error).
- **more than 1 argument** → `AssertionError: more than one argument is provided`.
- **argument not an integer** → `AssertionError: argument is not an integer`.
- Negative numbers are valid (`int("-5")` works; `-5 % 2 == 1` → Odd).

The `AssertionError` is raised, then caught in the `__main__` block and printed,
so the program never crashes with an uncaught traceback.

## Run
```
$> python whatis.py 14
I'm Even.
$> python whatis.py -5
I'm Odd.
$> python whatis.py
$> python whatis.py 0
I'm Even.
$> python whatis.py Hi!
AssertionError: argument is not an integer
$> python whatis.py 13 5
AssertionError: more than one argument is provided
```

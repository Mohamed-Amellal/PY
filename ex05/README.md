# Exercise 05 — First standalone program python

**File:** `building.py` · **Allowed:** `sys` or any lib to receive the args

> From here on: no code in the global scope, a real `main()`, docstrings on
> every function (`__doc__`), and code that passes `flake8`.

## Goal
Count, for a single string, the number of upper-case letters, lower-case
letters, punctuation marks, spaces and digits.

## Rules
- **1 argument** → analyze it.
- **0 arguments** → prompt `What is the text to count?` and read it. The
  carriage return you press counts as a **space** (that is why `"\n"` is
  appended to the input). Use `ctrl + D` if you don't want to send a return.
- **more than 1 argument** → `AssertionError`.
- Uses `str.isupper / islower / isspace / isdigit` and `string.punctuation`.

## Run
```
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits

$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
```

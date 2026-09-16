# Exercise 03 — NULL not found

**File:** `NULL_not_found.py` · **Allowed functions:** None

## Goal
`NULL_not_found(object: any) -> int` prints the type of every "Null" value and
returns `0` on success, `1` on error.

## The tricky ordering
`bool` is a **subclass of `int`** in Python, and `False == 0` is `True`. So the
checks must be ordered carefully:
1. `None`  → `NoneType`
2. `NaN`   → `float` (detected with `math.isnan`)
3. `bool`  → **before** `int`, otherwise `False` would be caught as `Zero`
4. `int` and `== 0` → `Zero`
5. `str` and `== ""` → `Empty`
6. else → `Type not Found`, `return 1`

Running `NULL_not_found.py` alone prints nothing.

## Run
```
$> python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty:  <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

# Exercise 06 — Recode filter + the program

**Files:** `ft_filter.py`, `filterstring.py` · **Allowed:** `sys` or any lib to
receive the args

## Part 1 — `ft_filter`
Recode the built-in `filter` **using a list comprehension**. Using the original
`filter` is forbidden.
- Its docstring is the same as `print(filter.__doc__)`.
- `function is None` → keep the items that are truthy.
- otherwise → keep the items for which `function(item)` is true.

## Part 2 — `filterstring.py`
Takes two arguments: a string **S** and an integer **N**. Prints the list of
words in **S** whose length is **strictly greater than N**.
- Words are split on spaces.
- Must contain **at least one list comprehension** and **one lambda** — here the
  `lambda word: len(word) > length` (the filter predicate) and the
  `[word for word in words]` comprehension.
- Wrong number of args, or a second argument that is not an integer →
  `AssertionError: the arguments are bad`.

## Run
```
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$> python filterstring.py 'Hello the World' 99
[]
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$> python filterstring.py
AssertionError: the arguments are bad
```

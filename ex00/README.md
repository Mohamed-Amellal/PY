# Exercise 00 — First python script

**File:** `Hello.py` · **Allowed functions:** None

## Goal
Modify the value stored in each data structure (list, tuple, set, dict) so the
program prints the campus greetings.

## Key points
- A **list** is mutable → reassign the item by index (`ft_list[1] = ...`).
- A **tuple** is immutable → you cannot assign an item; rebuild the whole tuple.
- A **set** is mutable but unordered → `remove()` the old value, `add()` the new.
- A **dict** → reassign through the key (`ft_dict["Hello"] = ...`).

## Run
```
$> python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'Morocco!')$
{'Hello', 'Benguerir!'}$
{'Hello': '1337Benguerir!'}$
$>
```
> Note: set order is not guaranteed, so the two set elements may print in the
> opposite order — that is normal.

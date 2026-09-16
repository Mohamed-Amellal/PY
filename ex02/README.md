# Exercise 02 — First function python

**File:** `find_ft_type.py` · **Allowed functions:** None

## Goal
Write `all_thing_is_obj(object: any) -> int` that prints the object's type and
returns `42`.

## Logic
- `list / tuple / set / dict` → `"<Name> : <class ...>"`.
- `str` → `"<value> is in the kitchen : <class 'str'>"`.
- anything else → `"Type not found"`.
- Always `return 42`.

Running `find_ft_type.py` alone prints **nothing** (it only defines a
function). Use `tester.py` (provided) to exercise it.

## Run
```
$> python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>

$> python find_ft_type.py | cat -e
$>
```

# Exercise 01 — First use of package

**File:** `format_ft_time.py` · **Allowed:** `time`, `datetime` or any lib that
gives the date.

## Goal
Print the current time in two representations, then today's date.

## Formatting explained
- `time.time()` → seconds elapsed since the Unix epoch (Jan 1, 1970).
- `{:,.4f}` → fixed-point with a thousands separator and 4 decimals
  (`1,666,355,857.3622`).
- `{:.2e}` → scientific notation with 2 decimals (`1.67e+09`).
- `datetime.now().strftime("%b %d %Y")` → abbreviated month, day, year
  (`Oct 21 2022`).

## Run
```
$> python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```
> Your numbers/date will differ from the example — only the **format** must
> match.

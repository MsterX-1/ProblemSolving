# Python Data Structures Complete Reference Guide

## Table of Contents

1. [list](#list)
2. [tuple](#tuple)
3. [str](#str)
4. [dict](#dict)
5. [set](#set)
6. [frozenset](#frozenset)
7. [collections.deque](#deque)
8. [collections.defaultdict](#defaultdict)
9. [collections.Counter](#counter)
10. [collections.OrderedDict](#ordereddict)
11. [collections.namedtuple](#namedtuple)
12. [heapq (Min-Heap)](#heapq)
13. [bisect (Sorted List)](#bisect)
14. [array.array (Typed Array)](#array)
15. [functools.lru_cache / cache (Memoization)](#lru_cache)
16. [math (Common Utilities)](#mathmod)
17. [sortedcontainers.SortedList](#sortedcontainers)
18. [Union-Find (Disjoint Set Union)](#unionfind)
19. [Trie](#trie)
20. [LeetCode Boilerplate (ListNode / TreeNode)](#boilerplate)

---

## list

<a id="list">list</a>

### When to Use

- Default dynamic-size ordered collection
- Frequent additions / removals at the **end**
- Random access by index required
- Most versatile, general-purpose sequence in Python

### Declaration

```python
lst = []
lst = [1, 2, 3]
lst = list(range(5))              # [0, 1, 2, 3, 4]
lst = [0] * 5                     # [0, 0, 0, 0, 0]
lst = [x**2 for x in range(5)]   # list comprehension
```

### Properties and Methods

| Method / Operation      | Time Complexity | Space Complexity | Description                              |
| ----------------------- | --------------- | ---------------- | ---------------------------------------- |
| `len(lst)`              | O(1)            | O(1)             | Number of elements                       |
| `lst[i]`                | O(1)            | O(1)             | Access by index                          |
| `lst[i] = x`            | O(1)            | O(1)             | Set by index                             |
| `lst[-i]`               | O(1)            | O(1)             | Access from end                          |
| `lst[i:j]`              | O(k)            | O(k)             | Slice (k = j − i)                        |
| `lst[i:j] = ...`        | O(n)            | O(k)             | Slice assignment                         |
| `x in lst`              | O(n)            | O(1)             | Membership test                          |
| `lst.append(x)`         | O(1) amortized  | O(1)             | Add to end                               |
| `lst.pop()`             | O(1)            | O(1)             | Remove and return last element           |
| `lst.pop(i)`            | O(n)            | O(1)             | Remove and return element at index       |
| `lst.insert(i, x)`      | O(n)            | O(1)             | Insert at index                          |
| `lst.remove(x)`         | O(n)            | O(1)             | Remove first occurrence                  |
| `lst.index(x)`          | O(n)            | O(1)             | Index of first occurrence                |
| `lst.count(x)`          | O(n)            | O(1)             | Count occurrences                        |
| `lst.sort()`            | O(n log n)      | O(n)             | Sort in-place (Timsort)                  |
| `sorted(lst)`           | O(n log n)      | O(n)             | Return new sorted list                   |
| `lst.reverse()`         | O(n)            | O(1)             | Reverse in-place                         |
| `reversed(lst)`         | O(1)            | O(1)             | Return reverse iterator                  |
| `lst.copy()`            | O(n)            | O(n)             | Shallow copy                             |
| `lst.clear()`           | O(n)            | O(1)             | Remove all elements                      |
| `lst.extend(iterable)`  | O(k)            | O(k)             | Append multiple (k = len of iterable)    |
| `lst + lst2`            | O(n + m)        | O(n + m)         | Concatenation                            |
| `lst * k`               | O(n·k)          | O(n·k)           | Repetition                               |
| `min(lst)`              | O(n)            | O(1)             | Minimum value                            |
| `max(lst)`              | O(n)            | O(1)             | Maximum value                            |
| `sum(lst)`              | O(n)            | O(1)             | Sum of values                            |
| `any(lst)`              | O(n)            | O(1)             | True if any element is truthy            |
| `all(lst)`              | O(n)            | O(1)             | True if all elements are truthy          |
| `enumerate(lst)`        | O(1)            | O(1)             | Returns (index, value) iterator          |
| `zip(lst1, lst2)`       | O(1)            | O(1)             | Pair elements (lazy)                     |

### Examples

```python
lst = [3, 1, 4, 1, 5]

# Access
print(lst[0])        # 3
print(lst[-1])       # 5
print(lst[1:3])      # [1, 4]

# Modify
lst.append(9)
print(lst)           # [3, 1, 4, 1, 5, 9]

lst.insert(2, 99)
print(lst)           # [3, 1, 99, 4, 1, 5, 9]

lst.remove(1)        # removes FIRST occurrence of 1
print(lst)           # [3, 99, 4, 1, 5, 9]

lst.pop()            # removes 9
lst.pop(0)           # removes 3
print(lst)           # [99, 4, 1, 5]

# Search
print(lst.index(4))  # 1
print(lst.count(1))  # 1
print(5 in lst)      # True

# Sort & Reverse
lst.sort()
print(lst)           # [1, 4, 5, 99]
lst.reverse()
print(lst)           # [99, 5, 4, 1]

# Aggregates
print(min(lst))      # 1
print(max(lst))      # 99
print(sum(lst))      # 109

# Sort with key
words = ["banana", "kiwi", "apple"]
words.sort(key=len)
print(words)         # ['kiwi', 'apple', 'banana']

words.sort(key=lambda x: x[-1])   # sort by last character
print(words)         # ['banana', 'kiwi', 'apple']

# Enumerate
for i, val in enumerate(lst):
    print(i, val)

# List comprehension
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]

# Zip
a = [1, 2, 3]
b = ['x', 'y', 'z']
paired = list(zip(a, b))   # [(1, 'x'), (2, 'y'), (3, 'z')]
d = dict(zip(a, b))        # {1: 'x', 2: 'y', 3: 'z'}
```

---

## tuple

<a id="tuple">tuple</a>

### When to Use

- Immutable ordered sequence (cannot change after creation)
- Return multiple values from a function
- As dictionary keys (tuples are hashable, lists are not)
- Slight memory/speed advantage over list when data is fixed

### Declaration

```python
t = ()
t = (1,)             # single-element tuple (comma required!)
t = (1, 2, 3)
t = 1, 2, 3          # parentheses are optional
t = tuple([1, 2, 3]) # from a list
```

### Properties and Methods

| Method / Operation | Time Complexity | Space Complexity | Description                            |
| ------------------ | --------------- | ---------------- | -------------------------------------- |
| `len(t)`           | O(1)            | O(1)             | Number of elements                     |
| `t[i]`             | O(1)            | O(1)             | Access by index                        |
| `t[i:j]`           | O(k)            | O(k)             | Slice (k = j − i)                      |
| `x in t`           | O(n)            | O(1)             | Membership test                        |
| `t.index(x)`       | O(n)            | O(1)             | Index of first occurrence              |
| `t.count(x)`       | O(n)            | O(1)             | Count occurrences                      |
| `t + t2`           | O(n + m)        | O(n + m)         | Concatenation (returns new tuple)      |
| `t * k`            | O(n·k)          | O(n·k)           | Repetition                             |
| `min(t)`           | O(n)            | O(1)             | Minimum value                          |
| `max(t)`           | O(n)            | O(1)             | Maximum value                          |
| `sum(t)`           | O(n)            | O(1)             | Sum of values                          |
| `sorted(t)`        | O(n log n)      | O(n)             | Returns a new sorted **list**          |
| `hash(t)`          | O(n)            | O(1)             | Hash value (elements must be hashable) |

### Examples

```python
t = (10, 20, 30, 20)

# Access
print(t[0])          # 10
print(t[-1])         # 20
print(t[1:3])        # (20, 30)

# Search
print(t.count(20))   # 2
print(t.index(30))   # 2
print(20 in t)       # True

# Aggregates
print(min(t))        # 10
print(max(t))        # 30
print(sum(t))        # 80

# Tuple unpacking
a, b, c, d = t
print(a, b)          # 10 20

# Extended unpacking
first, *rest = t
print(first, rest)   # 10 [20, 30, 20]

# Swap variables (uses tuple packing internally)
x, y = 1, 2
x, y = y, x
print(x, y)          # 2 1

# As dictionary key (lists cannot be used as keys)
coords = {(0, 0): "origin", (1, 2): "point A"}
print(coords[(1, 2)])    # point A
```

---

## str

<a id="str">str</a>

### When to Use

- Immutable text / character sequences
- Pattern matching, parsing, and text formatting
- Any text processing task

### Declaration

```python
s = "hello"
s = 'world'
s = """multi
line string"""
s = str(42)           # "42"
s = f"value: {42}"   # f-string (preferred formatting, Python 3.6+)
```

### Properties and Methods

| Method / Operation      | Time Complexity | Space Complexity | Description                                       |
| ----------------------- | --------------- | ---------------- | ------------------------------------------------- |
| `len(s)`                | O(1)            | O(1)             | Number of characters                              |
| `s[i]`                  | O(1)            | O(1)             | Access character by index                         |
| `s[i:j]`                | O(k)            | O(k)             | Slice (k = j − i)                                 |
| `x in s`                | O(n)            | O(1)             | Substring check                                   |
| `s.find(sub)`           | O(n)            | O(1)             | Index of first match; −1 if not found             |
| `s.rfind(sub)`          | O(n)            | O(1)             | Index of last match; −1 if not found              |
| `s.index(sub)`          | O(n)            | O(1)             | Like find, raises ValueError if not found         |
| `s.rindex(sub)`         | O(n)            | O(1)             | Like rfind, raises ValueError if not found        |
| `s.count(sub)`          | O(n)            | O(1)             | Count non-overlapping occurrences                 |
| `s.replace(old, new)`   | O(n)            | O(n)             | Replace all occurrences                           |
| `s.split(sep)`          | O(n)            | O(n)             | Split into list                                   |
| `s.rsplit(sep, n)`      | O(n)            | O(n)             | Split from right, up to n splits                  |
| `s.splitlines()`        | O(n)            | O(n)             | Split on line boundaries                          |
| `sep.join(lst)`         | O(n)            | O(n)             | Join iterable with separator                      |
| `s.strip()`             | O(n)            | O(n)             | Remove leading/trailing whitespace                |
| `s.lstrip()`            | O(n)            | O(n)             | Remove leading whitespace                         |
| `s.rstrip()`            | O(n)            | O(n)             | Remove trailing whitespace                        |
| `s.upper()`             | O(n)            | O(n)             | Convert to uppercase                              |
| `s.lower()`             | O(n)            | O(n)             | Convert to lowercase                              |
| `s.title()`             | O(n)            | O(n)             | Title case                                        |
| `s.capitalize()`        | O(n)            | O(n)             | First character upper, rest lower                 |
| `s.swapcase()`          | O(n)            | O(n)             | Swap upper/lower case                             |
| `s.startswith(prefix)`  | O(k)            | O(1)             | Check prefix (k = len of prefix)                  |
| `s.endswith(suffix)`    | O(k)            | O(1)             | Check suffix                                      |
| `s.isdigit()`           | O(n)            | O(1)             | All characters are digits                         |
| `s.isalpha()`           | O(n)            | O(1)             | All characters are alphabetic                     |
| `s.isalnum()`           | O(n)            | O(1)             | All characters are alphanumeric                   |
| `s.isspace()`           | O(n)            | O(1)             | All characters are whitespace                     |
| `s.isupper()`           | O(n)            | O(1)             | All cased characters are uppercase                |
| `s.islower()`           | O(n)            | O(1)             | All cased characters are lowercase                |
| `s.center(n, c)`        | O(n)            | O(n)             | Center in field of width n                        |
| `s.ljust(n, c)`         | O(n)            | O(n)             | Left-justify in field of width n                  |
| `s.rjust(n, c)`         | O(n)            | O(n)             | Right-justify in field of width n                 |
| `s.zfill(n)`            | O(n)            | O(n)             | Zero-pad on the left                              |
| `s.format(*args)`       | O(n)            | O(n)             | Format string                                     |
| `s.encode(enc)`         | O(n)            | O(n)             | Encode to bytes                                   |
| `b.decode(enc)`         | O(n)            | O(n)             | Decode bytes to str                               |
| `s.partition(sep)`      | O(n)            | O(n)             | Split into (before, sep, after)                   |
| `s.rpartition(sep)`     | O(n)            | O(n)             | Partition from the right                          |
| `ord(c)`                | O(1)            | O(1)             | Character → Unicode codepoint                     |
| `chr(i)`                | O(1)            | O(1)             | Unicode codepoint → character                     |

### Examples

```python
s = "Hello, World!"

# Access
print(s[0])           # H
print(s[-1])          # !
print(s[7:12])        # World

# Search
print(s.find("World"))     # 7
print(s.count("l"))        # 3
print("World" in s)        # True
print(s.startswith("He"))  # True
print(s.endswith("!"))     # True

# Transform (returns new string — str is immutable)
print(s.replace("World", "Python"))   # Hello, Python!
print(s.upper())                       # HELLO, WORLD!
print(s.lower())                       # hello, world!

# Split / Join
words = "one two three".split()        # ['one', 'two', 'three']
joined = "-".join(words)               # 'one-two-three'

csv = "a,b,c,d"
parts = csv.split(",")                 # ['a', 'b', 'c', 'd']
parts2 = csv.split(",", 2)            # ['a', 'b', 'c,d']  (max 2 splits)

# Strip
padded = "  hello  "
print(padded.strip())    # 'hello'

# Checks
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("a1b2".isalnum())   # True

# Padding
print("42".zfill(5))           # 00042
print("hi".center(10, '-'))    # ----hi----
print("hi".ljust(10, '.'))     # hi........
print("hi".rjust(10, '.'))     # ........hi

# f-strings (most efficient and readable)
name, age = "Yousef", 21
print(f"Name: {name}, Age: {age}")   # Name: Yousef, Age: 21
print(f"{3.14159:.2f}")              # 3.14
print(f"{42:08b}")                   # 00101010  (binary, zero-padded)

# ord / chr
print(ord('A'))    # 65
print(chr(65))     # A
print(chr(ord('a') + 3))   # d

# String as character sequence
chars = list("hello")       # ['h', 'e', 'l', 'l', 'o']
rebuilt = "".join(chars)    # 'hello'
reversed_s = "".join(reversed("hello"))   # 'olleh'
```

---

## dict

<a id="dict">dict</a>

### When to Use

- Key-value storage with fast O(1) lookup
- Counting element frequencies
- Caching / memoization
- Lookup tables and mappings
- Grouping or indexing data

> **Note**: As of Python 3.7, `dict` preserves **insertion order** as a language guarantee.

### Declaration

```python
d = {}
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d = dict([("a", 1), ("b", 2)])
d = {k: v for k, v in zip("abc", [1, 2, 3])}  # dict comprehension
d = dict.fromkeys(["x", "y", "z"], 0)          # all values = 0
```

### Properties and Methods

| Method / Operation         | Time Complexity | Space Complexity | Description                                |
| -------------------------- | --------------- | ---------------- | ------------------------------------------ |
| `len(d)`                   | O(1)            | O(1)             | Number of key-value pairs                  |
| `d[key]`                   | O(1) avg        | O(1)             | Access by key (raises KeyError if missing) |
| `d[key] = val`             | O(1) avg        | O(1)             | Set or update a key                        |
| `del d[key]`               | O(1) avg        | O(1)             | Delete key (raises KeyError if missing)    |
| `key in d`                 | O(1) avg        | O(1)             | Membership test (checks keys)              |
| `key not in d`             | O(1) avg        | O(1)             | Non-membership test                        |
| `d.get(key)`               | O(1) avg        | O(1)             | Safe access, returns None if missing       |
| `d.get(key, default)`      | O(1) avg        | O(1)             | Safe access with custom default            |
| `d.keys()`                 | O(1)            | O(1)             | View of all keys                           |
| `d.values()`               | O(1)            | O(1)             | View of all values                         |
| `d.items()`                | O(1)            | O(1)             | View of all (key, value) pairs             |
| `d.pop(key)`               | O(1) avg        | O(1)             | Remove and return value                    |
| `d.pop(key, default)`      | O(1) avg        | O(1)             | Remove with fallback default               |
| `d.popitem()`              | O(1)            | O(1)             | Remove and return last inserted pair       |
| `d.update(d2)`             | O(m)            | O(1)             | Merge another dict (m = len of d2)         |
| `d.setdefault(key, val)`   | O(1) avg        | O(1)             | Set if missing, return current value       |
| `d.clear()`                | O(n)            | O(1)             | Remove all pairs                           |
| `d.copy()`                 | O(n)            | O(n)             | Shallow copy                               |
| `dict.fromkeys(iter, val)` | O(n)            | O(n)             | Create dict from keys                      |
| `{**d1, **d2}`             | O(n + m)        | O(n + m)         | Merge dicts (Python 3.5+); d2 wins         |
| `d1 \| d2`                 | O(n + m)        | O(n + m)         | Merge (Python 3.9+); d2 wins              |
| `d1 \|= d2`                | O(m)            | O(1)             | In-place merge (Python 3.9+)               |

### Examples

```python
d = {"name": "Yousef", "age": 21}

# Access
print(d["name"])               # Yousef
print(d.get("age"))            # 21
print(d.get("city", "N/A"))   # N/A  (no KeyError)

# Modify
d["city"] = "Alexandria"
d["age"] = 22
del d["city"]
print(d)   # {'name': 'Yousef', 'age': 22}

# Views
print(list(d.keys()))     # ['name', 'age']
print(list(d.values()))   # ['Yousef', 22]
print(list(d.items()))    # [('name', 'Yousef'), ('age', 22)]

# Iteration
for key, val in d.items():
    print(f"{key}: {val}")

# Pop
age = d.pop("age")
print(age)   # 22

# setdefault (common pattern for grouping)
groups = {}
for word in ["apple", "banana", "avocado", "blueberry"]:
    groups.setdefault(word[0], []).append(word)
print(groups)   # {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}

# Merge
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = {**d1, **d2}       # {'a': 1, 'b': 99, 'c': 3}  (d2 wins on overlap)
merged = d1 | d2            # same, Python 3.9+

# Dict comprehension
squares = {x: x**2 for x in range(5)}         # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
filtered = {k: v for k, v in squares.items() if v > 4}  # {3: 9, 4: 16}

# Frequency count
text = "hello world"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)   # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

---

## set

<a id="set">set</a>

### When to Use

- Unique elements (no duplicates allowed)
- Fast O(1) membership testing
- Set algebra: union, intersection, difference
- Removing duplicates from a sequence

### Declaration

```python
s = set()
s = {1, 2, 3}
s = set([1, 2, 2, 3])        # {1, 2, 3} — duplicates dropped
s = {x for x in range(5)}    # set comprehension
```

### Properties and Methods

| Method / Operation                          | Time Complexity     | Space Complexity | Description                            |
| ------------------------------------------- | ------------------- | ---------------- | -------------------------------------- |
| `len(s)`                                    | O(1)                | O(1)             | Number of elements                     |
| `x in s`                                    | O(1) avg            | O(1)             | Membership test                        |
| `s.add(x)`                                  | O(1) avg            | O(1)             | Add element                            |
| `s.remove(x)`                               | O(1) avg            | O(1)             | Remove element (raises KeyError)       |
| `s.discard(x)`                              | O(1) avg            | O(1)             | Remove element (no error if missing)   |
| `s.pop()`                                   | O(1)                | O(1)             | Remove and return arbitrary element    |
| `s.clear()`                                 | O(n)                | O(1)             | Remove all elements                    |
| `s.copy()`                                  | O(n)                | O(n)             | Shallow copy                           |
| `s.union(t)` / `s \| t`                     | O(n + m)            | O(n + m)         | Union                                  |
| `s.intersection(t)` / `s & t`               | O(min(n, m))        | O(n)             | Intersection                           |
| `s.difference(t)` / `s - t`                 | O(n)                | O(n)             | Elements in s but not in t             |
| `s.symmetric_difference(t)` / `s ^ t`       | O(n + m)            | O(n + m)         | Elements in either but not both        |
| `s.issubset(t)` / `s <= t`                  | O(n)                | O(1)             | Check if s ⊆ t                         |
| `s.issuperset(t)` / `s >= t`                | O(m)                | O(1)             | Check if s ⊇ t                         |
| `s.isdisjoint(t)`                           | O(min(n, m))        | O(1)             | Check if no elements in common         |
| `s.update(t)` / `s \|= t`                  | O(m)                | O(m)             | Add all elements from t                |
| `s.intersection_update(t)` / `s &= t`       | O(n)                | O(1)             | Keep only common elements              |
| `s.difference_update(t)` / `s -= t`         | O(m)                | O(1)             | Remove elements that are in t          |
| `s.symmetric_difference_update(t)` / `s ^= t` | O(n + m)          | O(n)             | Keep only non-common elements          |

### Examples

```python
s = {1, 2, 3, 4}

# Add / Remove
s.add(5)
s.discard(99)    # no error even though 99 is not there
s.remove(1)
print(s)         # {2, 3, 4, 5}

# Membership
print(3 in s)    # True
print(10 in s)   # False

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}  — union
print(a & b)   # {3, 4}              — intersection
print(a - b)   # {1, 2}              — difference
print(a ^ b)   # {1, 2, 5, 6}       — symmetric difference

# Subset / Superset
print({1, 2} <= {1, 2, 3})           # True (subset)
print({1, 2, 3} >= {1, 2})           # True (superset)
print({1, 2}.isdisjoint({3, 4}))     # True

# Remove duplicates from a list (order not preserved)
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))
print(unique)   # [1, 2, 3, 4]

# To keep order while deduplicating (Python 3.7+)
seen = set()
unique_ordered = [x for x in lst if not (x in seen or seen.add(x))]
print(unique_ordered)   # [1, 2, 3, 4]

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)   # {0, 4, 16, 36, 64}
```

---

## frozenset

<a id="frozenset">frozenset</a>

### When to Use

- Immutable, hashable version of `set`
- Using a set as a dictionary key
- When a set must not be modified (thread-safe, safe to cache)

### Declaration

```python
fs = frozenset()
fs = frozenset([1, 2, 3, 2])   # frozenset({1, 2, 3})
fs = frozenset("hello")         # frozenset({'h', 'e', 'l', 'o'})
```

### Properties and Methods

All non-mutating `set` methods apply. Mutating methods (`add`, `remove`, `discard`, `pop`, `clear`, `update`, etc.) are **not available**.

| Method / Operation             | Time Complexity | Space Complexity | Description                            |
| ------------------------------ | --------------- | ---------------- | -------------------------------------- |
| `len(fs)`                      | O(1)            | O(1)             | Number of elements                     |
| `x in fs`                      | O(1) avg        | O(1)             | Membership test                        |
| `fs.union(t)` / `fs \| t`      | O(n + m)        | O(n + m)         | Union (returns frozenset)              |
| `fs.intersection(t)` / `fs & t` | O(min(n, m))   | O(n)             | Intersection                           |
| `fs.difference(t)` / `fs - t`  | O(n)            | O(n)             | Difference                             |
| `fs.issubset(t)` / `fs <= t`   | O(n)            | O(1)             | Subset check                           |
| `fs.issuperset(t)` / `fs >= t` | O(m)            | O(1)             | Superset check                         |
| `fs.isdisjoint(t)`             | O(min(n, m))    | O(1)             | Disjoint check                         |
| `fs.copy()`                    | O(n)            | O(n)             | Copy (returns frozenset)               |
| `hash(fs)`                     | O(n)            | O(1)             | Hash value                             |

### Examples

```python
fs = frozenset([1, 2, 3])

# Cannot mutate
# fs.add(4)   -> AttributeError

# As a dictionary key (impossible with regular set)
cache = {
    frozenset([1, 2]): "pair",
    frozenset([3]):    "single"
}
print(cache[frozenset([1, 2])])   # pair

# Set operations return frozenset
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a & b)   # frozenset({2, 3})
print(a | b)   # frozenset({1, 2, 3, 4})
print(a - b)   # frozenset({1})
```

---

## collections.deque

<a id="deque">collections.deque</a>

### When to Use

- Double-ended queue: fast append/pop on **both** ends — O(1) vs list's O(n) at the front
- Implementing stacks and queues without the O(n) penalty
- BFS (Breadth-First Search)
- Sliding window algorithms
- Bounded circular buffer (use `maxlen`)

### Declaration

```python
from collections import deque
d = deque()
d = deque([1, 2, 3])
d = deque([1, 2, 3], maxlen=5)   # bounded — auto-evicts oldest when full
```

### Properties and Methods

| Method / Operation    | Time Complexity | Space Complexity | Description                                       |
| --------------------- | --------------- | ---------------- | ------------------------------------------------- |
| `len(d)`              | O(1)            | O(1)             | Number of elements                                |
| `d[0]` / `d[-1]`     | O(1)            | O(1)             | Access first / last element                       |
| `d[i]`                | O(n)            | O(1)             | Access by arbitrary index                         |
| `d.append(x)`         | O(1)            | O(1)             | Add to right end                                  |
| `d.appendleft(x)`     | O(1)            | O(1)             | Add to left end                                   |
| `d.pop()`             | O(1)            | O(1)             | Remove and return from right                      |
| `d.popleft()`         | O(1)            | O(1)             | Remove and return from left                       |
| `d.extend(iterable)`  | O(k)            | O(k)             | Extend right (k = len of iterable)                |
| `d.extendleft(iterable)` | O(k)         | O(k)             | Extend left (each element prepended — reverses order) |
| `d.rotate(n)`         | O(n)            | O(1)             | Rotate right if n > 0, left if n < 0              |
| `d.count(x)`          | O(n)            | O(1)             | Count occurrences                                 |
| `d.index(x)`          | O(n)            | O(1)             | Index of first occurrence                         |
| `d.insert(i, x)`      | O(n)            | O(1)             | Insert at index i                                 |
| `d.remove(x)`         | O(n)            | O(1)             | Remove first occurrence                           |
| `d.reverse()`         | O(n)            | O(1)             | Reverse in-place                                  |
| `d.clear()`           | O(n)            | O(1)             | Remove all elements                               |
| `d.copy()`            | O(n)            | O(n)             | Shallow copy                                      |
| `d.maxlen`            | O(1)            | O(1)             | Max length (None if unbounded)                    |
| `x in d`              | O(n)            | O(1)             | Membership test                                   |

### Examples

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)          # deque([1, 2, 3, 4])
d.appendleft(0)      # deque([0, 1, 2, 3, 4])
d.pop()              # returns 4 → deque([0, 1, 2, 3])
d.popleft()          # returns 0 → deque([1, 2, 3])

# Use as a stack (LIFO)
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())   # 3

# Use as a queue (FIFO)
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())   # 1

# Bounded deque — auto-evicts oldest when full
buf = deque(maxlen=3)
for i in range(5):
    buf.append(i)
print(buf)   # deque([2, 3, 4], maxlen=3)

# Rotate
d = deque([1, 2, 3, 4, 5])
d.rotate(2)       # right: deque([4, 5, 1, 2, 3])
d.rotate(-2)      # left:  deque([1, 2, 3, 4, 5])

# BFS traversal
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
print(bfs(graph, 1))   # [1, 2, 3, 4]
```

---

## collections.defaultdict

<a id="defaultdict">collections.defaultdict</a>

### When to Use

- Dict that auto-creates a default value for missing keys
- Grouping items without checking if a key exists first
- Counting (use `int` as the factory)
- Building graph adjacency lists

### Declaration

```python
from collections import defaultdict
d = defaultdict(int)            # missing key → 0
d = defaultdict(list)           # missing key → []
d = defaultdict(set)            # missing key → set()
d = defaultdict(str)            # missing key → ""
d = defaultdict(lambda: "N/A")  # custom default
```

### Properties and Methods

All standard `dict` methods apply. The key difference is missing-key behavior:

| Method / Operation    | Time Complexity | Space Complexity | Description                                      |
| --------------------- | --------------- | ---------------- | ------------------------------------------------ |
| `d[missing_key]`      | O(1) avg        | O(1)             | Calls `default_factory()` and stores the result  |
| `d.default_factory`   | O(1)            | O(1)             | The factory callable (readable / settable)       |

All other operations are identical to `dict`.

### Examples

```python
from collections import defaultdict

# Counting words
word_count = defaultdict(int)
for word in "the cat sat on the mat".split():
    word_count[word] += 1
print(dict(word_count))   # {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}

# Grouping by key
groups = defaultdict(list)
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
for key, val in data:
    groups[key].append(val)
print(dict(groups))   # {'a': [1, 3], 'b': [2, 4]}

# Graph adjacency list
graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # undirected
print(dict(graph))   # {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}

# Nested defaultdict (2D table)
table = defaultdict(lambda: defaultdict(int))
table["row1"]["col1"] += 1
table["row1"]["col2"] += 5
print(dict(table["row1"]))   # {'col1': 1, 'col2': 5}
```

---

## collections.Counter

<a id="counter">collections.Counter</a>

### When to Use

- Count frequencies of elements in an iterable
- Most / least common elements
- Multiset (bag) arithmetic
- Anagram detection / character frequency comparison

### Declaration

```python
from collections import Counter
c = Counter()
c = Counter([1, 2, 2, 3, 3, 3])       # Counter({3: 3, 2: 2, 1: 1})
c = Counter("mississippi")             # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c = Counter({"a": 3, "b": 1})
```

### Properties and Methods

| Method / Operation        | Time Complexity | Space Complexity | Description                                        |
| ------------------------- | --------------- | ---------------- | -------------------------------------------------- |
| `Counter(iterable)`       | O(n)            | O(k)             | Create counter (k = number of unique elements)     |
| `c[key]`                  | O(1) avg        | O(1)             | Get count (returns 0 if missing, no KeyError)      |
| `c.most_common(n)`        | O(k log n)      | O(k)             | Top n most common elements                         |
| `c.most_common()`         | O(k log k)      | O(k)             | All elements sorted by count descending            |
| `c.elements()`            | O(n)            | O(1)             | Iterator over elements repeated by count           |
| `c.subtract(other)`       | O(n)            | O(1)             | Subtract counts (allows negative)                  |
| `c.update(other)`         | O(n)            | O(1)             | Add counts                                         |
| `c.total()`               | O(k)            | O(1)             | Sum of all counts (Python 3.10+)                   |
| `c1 + c2`                 | O(n)            | O(n)             | Add counts (drops zero / negative)                 |
| `c1 - c2`                 | O(n)            | O(n)             | Subtract counts (drops zero / negative)            |
| `c1 & c2`                 | O(n)            | O(n)             | Minimum of counts (intersection)                   |
| `c1 \| c2`                | O(n)            | O(n)             | Maximum of counts (union)                          |
| `sum(c.values())`         | O(k)            | O(1)             | Total element count (all k unique keys)            |
| `len(c)`                  | O(1)            | O(1)             | Number of unique elements                          |

### Examples

```python
from collections import Counter

# Count characters
c = Counter("abracadabra")
print(c)                     # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c['a'])                # 5
print(c['z'])                # 0  (no KeyError!)
print(c.most_common(3))      # [('a', 5), ('b', 2), ('r', 2)]

# Count words
words = "the quick brown fox jumps over the lazy dog the".split()
wc = Counter(words)
print(wc.most_common(2))     # [('the', 3), ('quick', 1)]

# Arithmetic
c1 = Counter("aab")          # {'a': 2, 'b': 1}
c2 = Counter("bbc")          # {'b': 2, 'c': 1}
print(c1 + c2)   # Counter({'b': 3, 'a': 2, 'c': 1})
print(c1 - c2)   # Counter({'a': 2})             (negative/zero dropped)
print(c1 & c2)   # Counter({'b': 1})             (min of each count)
print(c1 | c2)   # Counter({'a': 2, 'b': 2, 'c': 1})  (max of each count)

# Anagram check
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False

# elements() — repeated iteration
c = Counter(a=3, b=2)
print(list(c.elements()))   # ['a', 'a', 'a', 'b', 'b']

# Subtract (allows negatives unlike -)
c = Counter("aaab")
c.subtract(Counter("aac"))
print(c)   # Counter({'b': 1, 'a': 1, 'c': -1})
```

---

## collections.OrderedDict

<a id="ordereddict">collections.OrderedDict</a>

### When to Use

- LRU cache implementation using `move_to_end()`
- When you need to **reorder** existing keys (not possible with regular dict)
- Pre-Python 3.7 code that requires guaranteed ordering

> **Note**: In Python 3.7+, plain `dict` guarantees insertion order. Use `OrderedDict` only when you specifically need `move_to_end()` or `popitem(last=False)`.

### Declaration

```python
from collections import OrderedDict
od = OrderedDict()
od = OrderedDict([("a", 1), ("b", 2)])
od = OrderedDict(a=1, b=2)
```

### Properties and Methods

All `dict` methods apply, plus:

| Method / Operation            | Time Complexity | Space Complexity | Description                                  |
| ----------------------------- | --------------- | ---------------- | -------------------------------------------- |
| `od.move_to_end(key)`         | O(1)            | O(1)             | Move key to end (`last=True`) or start       |
| `od.move_to_end(key, last=False)` | O(1)        | O(1)             | Move key to front                            |
| `od.popitem(last=True)`       | O(1)            | O(1)             | Remove and return last (or first) inserted   |

### Examples

```python
from collections import OrderedDict

od = OrderedDict()
od["b"] = 2
od["a"] = 1
od["c"] = 3
print(list(od.keys()))   # ['b', 'a', 'c']

# Move to end / front
od.move_to_end("b")              # → ['a', 'c', 'b']
od.move_to_end("b", last=False)  # → ['b', 'a', 'c']

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)   # evict least recently used

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))    # 1
lru.put(3, 3)        # evicts key 2
print(lru.get(2))    # -1 (evicted)
print(lru.get(3))    # 3
```

---

## collections.namedtuple

<a id="namedtuple">collections.namedtuple</a>

### When to Use

- Immutable records with named, readable fields
- Lightweight alternative to a class when only data is needed
- Readable multiple return values from a function
- CSV/tabular row representation

### Declaration

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
Point = namedtuple("Point", "x y")    # space-separated string also works

# Python 3.6+ typed version (preferred for new code)
from typing import NamedTuple
class Point(NamedTuple):
    x: float
    y: float
    label: str = "origin"   # default value supported
```

### Properties and Methods

All `tuple` methods apply, plus:

| Method / Operation       | Time Complexity | Space Complexity | Description                                  |
| ------------------------ | --------------- | ---------------- | -------------------------------------------- |
| `p.field_name`           | O(1)            | O(1)             | Access field by name                         |
| `p[i]`                   | O(1)            | O(1)             | Access field by index                        |
| `p._asdict()`            | O(n)            | O(n)             | Convert to an OrderedDict                    |
| `p._replace(**kwargs)`   | O(n)            | O(n)             | Return a new instance with changed fields    |
| `Type._fields`           | O(1)            | O(1)             | Tuple of field names                         |
| `Type._make(iterable)`   | O(n)            | O(n)             | Create instance from an iterable             |
| `Type._field_defaults`   | O(1)            | O(1)             | Dict of fields with defaults                 |

### Examples

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

# Access
print(p.x, p.y)    # 3 4
print(p[0], p[1])  # 3 4

# Immutable
# p.x = 10  → AttributeError

# Replace (returns new instance)
p2 = p._replace(x=10)
print(p2)            # Point(x=10, y=4)

# As dict
print(p._asdict())   # {'x': 3, 'y': 4}

# From iterable
p3 = Point._make([5, 6])
print(p3)            # Point(x=5, y=6)

# Useful for tabular data
Student = namedtuple("Student", ["name", "grade", "age"])
students = [
    Student("Alice", "A", 20),
    Student("Bob",   "B", 22),
]
for s in students:
    print(f"{s.name}: grade {s.grade}")

# Typed NamedTuple with defaults
from typing import NamedTuple

class Config(NamedTuple):
    host: str
    port: int = 8080
    debug: bool = False

c = Config("localhost")
print(c.host, c.port, c.debug)   # localhost 8080 False
```

---

## heapq (Min-Heap)

<a id="heapq">heapq (Min-Heap)</a>

### When to Use

- Priority queue: always access the **minimum** element in O(1)
- K-th largest / smallest element
- Dijkstra's shortest path, A* search
- Merging sorted iterables

> **Note**: Python's `heapq` is a **min-heap**. For a max-heap, push **negated** values.

### Declaration

```python
import heapq
heap = []                        # just a plain list
heapq.heappush(heap, x)          # push and maintain heap invariant

# Build from existing list — O(n), more efficient than n pushes
lst = [5, 3, 1, 4, 2]
heapq.heapify(lst)               # lst is now a valid min-heap in-place
```

### Properties and Methods

| Method / Operation              | Time Complexity | Space Complexity | Description                                       |
| ------------------------------- | --------------- | ---------------- | ------------------------------------------------- |
| `heapq.heappush(h, x)`          | O(log n)        | O(1)             | Push item onto heap                               |
| `heapq.heappop(h)`              | O(log n)        | O(1)             | Pop and return the smallest item                  |
| `h[0]`                          | O(1)            | O(1)             | Peek at smallest item (no removal)                |
| `heapq.heappushpop(h, x)`       | O(log n)        | O(1)             | Push x, then pop and return the smallest          |
| `heapq.heapreplace(h, x)`       | O(log n)        | O(1)             | Pop smallest, then push x (more efficient)        |
| `heapq.heapify(lst)`            | O(n)            | O(1)             | Convert list to heap in-place                     |
| `heapq.nlargest(k, iterable)`   | O(n log k)      | O(k)             | Return k largest elements                         |
| `heapq.nsmallest(k, iterable)`  | O(n log k)      | O(k)             | Return k smallest elements                        |
| `heapq.merge(*iterables)`       | O(n log k)      | O(k)             | Merge k sorted iterables lazily                   |
| `len(h)`                        | O(1)            | O(1)             | Number of elements                                |

### Examples

```python
import heapq

# Min-heap basics
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(h[0])                  # 1  (peek minimum)
print(heapq.heappop(h))      # 1
print(heapq.heappop(h))      # 3
print(heapq.heappop(h))      # 5

# Build heap from list (O(n))
lst = [5, 3, 1, 4, 2]
heapq.heapify(lst)
print(lst[0])                # 1

# Max-heap — negate values
h = []
for x in [5, 1, 3]:
    heapq.heappush(h, -x)
print(-heapq.heappop(h))     # 5 (maximum)

# K largest / K smallest
nums = [3, 1, 5, 12, 2, 11]
print(heapq.nlargest(3, nums))    # [12, 11, 5]
print(heapq.nsmallest(3, nums))   # [1, 2, 3]

# Priority queue using (priority, data) tuples
tasks = []
heapq.heappush(tasks, (3, "Low priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappush(tasks, (2, "Medium priority task"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"[{priority}] {task}")
# [1] High priority task
# [2] Medium priority task
# [3] Low priority task

# Merge sorted iterables
sorted_a = [1, 3, 5]
sorted_b = [2, 4, 6]
merged = list(heapq.merge(sorted_a, sorted_b))
print(merged)   # [1, 2, 3, 4, 5, 6]

# Dijkstra's shortest path
def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue   # stale entry — skip
        for neighbor, weight in graph.get(node, []):
            new_d = d + weight
            if new_d < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_d
                heapq.heappush(heap, (new_d, neighbor))
    return dist

graph = {0: [(1, 4), (2, 1)], 2: [(1, 2), (3, 5)], 1: [(3, 1)], 3: []}
print(dijkstra(graph, 0))   # {0: 0, 1: 3, 2: 1, 3: 4}
```

---

## bisect (Sorted List)

<a id="bisect">bisect (Sorted List)</a>

### When to Use

- Binary search on a sorted list
- Maintaining sorted order when inserting elements
- Finding nearest element / range boundaries efficiently

> **Warning**: `insort` is O(n) overall because list insertion shifts elements, even though the binary search itself is O(log n). For a true O(log n) sorted structure use the third-party `sortedcontainers.SortedList`.

### Declaration

```python
import bisect
lst = [1, 3, 5, 7, 9]   # list must be sorted!
```

### Properties and Methods

| Method / Operation           | Time Complexity | Space Complexity | Description                                      |
| ---------------------------- | --------------- | ---------------- | ------------------------------------------------ |
| `bisect.bisect_left(a, x)`   | O(log n)        | O(1)             | Leftmost index to insert x (before equal values) |
| `bisect.bisect_right(a, x)`  | O(log n)        | O(1)             | Rightmost index to insert x (after equal values) |
| `bisect.bisect(a, x)`        | O(log n)        | O(1)             | Alias for `bisect_right`                         |
| `bisect.insort_left(a, x)`   | O(n)            | O(1)             | Insert x at leftmost position maintaining order  |
| `bisect.insort_right(a, x)`  | O(n)            | O(1)             | Insert x at rightmost position                   |
| `bisect.insort(a, x)`        | O(n)            | O(1)             | Alias for `insort_right`                         |

### Examples

```python
import bisect

lst = [1, 3, 5, 7, 9]

# Find insertion position
print(bisect.bisect_left(lst, 4))    # 2 (insert before index 2)
print(bisect.bisect_right(lst, 5))   # 3 (insert after existing 5)

# Difference between left and right on duplicate values
lst2 = [1, 3, 3, 3, 7]
print(bisect.bisect_left(lst2, 3))   # 1  (first 3)
print(bisect.bisect_right(lst2, 3))  # 4  (after last 3)

# Binary search — check if value exists
def contains(a, x):
    i = bisect.bisect_left(a, x)
    return i < len(a) and a[i] == x

print(contains(lst, 5))   # True
print(contains(lst, 4))   # False

# Count of a value in sorted list
def count_sorted(a, x):
    return bisect.bisect_right(a, x) - bisect.bisect_left(a, x)

print(count_sorted(lst2, 3))   # 3

# Insert maintaining order
lst = [1, 3, 5]
bisect.insort(lst, 4)
print(lst)   # [1, 3, 4, 5]

# Grade lookup (classic bisect pattern)
breakpoints = [60, 70, 80, 90]
grades = "FDCBA"

def grade(score):
    return grades[bisect.bisect(breakpoints, score)]

print(grade(55))   # F
print(grade(72))   # C
print(grade(90))   # A

# Find nearest element
def find_nearest(a, x):
    i = bisect.bisect_left(a, x)
    if i == 0:
        return a[0]
    if i == len(a):
        return a[-1]
    before, after = a[i - 1], a[i]
    return before if abs(before - x) <= abs(after - x) else after

print(find_nearest([1, 3, 6, 10], 4))   # 3
```

---

## array.array (Typed Array)

<a id="array">array.array (Typed Array)</a>

### When to Use

- Memory-efficient storage of large numeric arrays of **uniform type**
- When you need roughly half the memory of an equivalent `list`
- Binary I/O and C-level interoperability
- When `numpy` is unavailable

> **Common typecodes**: `'b'` signed char · `'B'` unsigned char · `'i'` signed int · `'I'` unsigned int · `'l'` signed long · `'f'` float (4 B) · `'d'` double (8 B)

### Declaration

```python
from array import array
a = array('i', [1, 2, 3, 4])   # signed int array
a = array('d', [1.0, 2.5])     # double float array
a = array('b', range(10))      # signed char array
```

### Properties and Methods

| Method / Operation   | Time Complexity | Space Complexity | Description                                  |
| -------------------- | --------------- | ---------------- | -------------------------------------------- |
| `len(a)`             | O(1)            | O(1)             | Number of elements                           |
| `a[i]`               | O(1)            | O(1)             | Access by index                              |
| `a[i] = x`           | O(1)            | O(1)             | Set by index                                 |
| `a[i:j]`             | O(k)            | O(k)             | Slice                                        |
| `x in a`             | O(n)            | O(1)             | Membership test                              |
| `a.append(x)`        | O(1) amortized  | O(1)             | Add to end                                   |
| `a.pop()`            | O(1)            | O(1)             | Remove last element                          |
| `a.pop(i)`           | O(n)            | O(1)             | Remove at index                              |
| `a.insert(i, x)`     | O(n)            | O(1)             | Insert at index                              |
| `a.remove(x)`        | O(n)            | O(1)             | Remove first occurrence                      |
| `a.index(x)`         | O(n)            | O(1)             | Index of first occurrence                    |
| `a.count(x)`         | O(n)            | O(1)             | Count occurrences                            |
| `a.reverse()`        | O(n)            | O(1)             | Reverse in-place                             |
| `a.extend(iterable)` | O(k)            | O(k)             | Extend from iterable                         |
| `a.tolist()`         | O(n)            | O(n)             | Convert to plain list                        |
| `a.tobytes()`        | O(n)            | O(n)             | Convert to bytes object                      |
| `a.frombytes(b)`     | O(n)            | O(n)             | Append items from bytes                      |
| `a.typecode`         | O(1)            | O(1)             | Type code character ('i', 'd', etc.)         |
| `a.itemsize`         | O(1)            | O(1)             | Bytes per element                            |

### Examples

```python
from array import array

a = array('i', [10, 20, 30, 40, 50])

# Access
print(a[0])       # 10
print(a[-1])      # 50
print(a[1:3])     # array('i', [20, 30])

# Modify
a.append(60)
a.insert(0, 5)
a.remove(20)
print(a)          # array('i', [5, 10, 30, 40, 50, 60])

# Convert
lst = a.tolist()
print(lst)        # [5, 10, 30, 40, 50, 60]

# Binary I/O
raw = a.tobytes()
b = array('i')
b.frombytes(raw)
print(b == a)     # True

# Memory comparison
import sys
lst = list(range(10_000))
arr = array('i', range(10_000))
print(sys.getsizeof(lst))                           # ~85 KB
print(arr.buffer_info()[1] * arr.itemsize)          # ~40 KB  (~2× smaller)
```

---

## functools.lru_cache / cache

<a id="lru_cache">functools.lru_cache / cache</a>

### When to Use

- Memoizing recursive functions (top-down DP) — turns exponential recursion into linear/polynomial
- Avoiding recomputation of expensive pure functions
- Classic candidates: Fibonacci, climbing stairs, edit distance, any "overlapping subproblems" recursion

> **Warning**: All arguments must be **hashable** (ints, strings, tuples — not lists/dicts/sets).

### Declaration

```python
from functools import lru_cache, cache

@lru_cache(maxsize=None)   # unbounded cache
def fib(n):
    ...

@cache   # Python 3.9+, shorthand for lru_cache(maxsize=None)
def fib(n):
    ...
```

### Properties and Methods

| Method / Operation         | Time Complexity | Space Complexity | Description                                    |
| --------------------------- | --------------- | ----------------- | ----------------------------------------------- |
| `@lru_cache(maxsize=None)`  | O(1) lookup      | O(k)               | Memoizes return values keyed by argument tuple  |
| `@cache`                    | O(1) lookup      | O(k)               | Shorthand for `lru_cache(maxsize=None)` (3.9+)  |
| `func.cache_clear()`        | O(1)             | O(1)               | Clear all cached entries                        |
| `func.cache_info()`         | O(1)             | O(1)               | Returns hits/misses/maxsize/currsize             |

### Examples

```python
from functools import lru_cache, cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(35))            # instant — without caching this is exponential
print(fib.cache_info())   # CacheInfo(hits=33, misses=36, maxsize=None, currsize=36)
fib.cache_clear()

# Climbing stairs (classic DP recursion)
@cache
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(10))   # 89

# functools.reduce — fold a sequence into a single value
from functools import reduce
product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(product)             # 24
```

---

## math (Common Utilities)

<a id="mathmod">math (Common Utilities)</a>

### When to Use

- Infinity sentinels for "no answer yet" tracking
- GCD/LCM for number-theory problems
- Exact integer square roots, factorials, combinatorics (nCr, nPr)
- Anything you'd otherwise hand-roll with `**0.5` and risk float precision bugs

### Declaration

```python
import math
```

### Properties and Methods

| Method / Operation         | Time Complexity   | Space Complexity | Description                                         |
| --------------------------- | ------------------ | ----------------- | ---------------------------------------------------- |
| `math.inf` / `-math.inf`   | O(1)                | O(1)               | Floating-point infinity sentinel                     |
| `math.gcd(*ints)`           | O(log(min))         | O(1)               | Greatest common divisor (3.9+ supports 2+ args)      |
| `math.lcm(*ints)`           | O(log(min))         | O(1)               | Least common multiple (3.9+)                         |
| `math.isqrt(n)`             | O(log n)            | O(1)               | Exact integer floor square root (no float error)     |
| `math.factorial(n)`         | O(n)                | O(1)               | n!                                                    |
| `math.comb(n, k)`           | O(min(k, n−k))      | O(1)               | n choose k                                            |
| `math.perm(n, k)`           | O(k)                | O(1)               | nPk permutations                                      |
| `math.log2(x)` / `math.log(x, base)` | O(1)       | O(1)               | Logarithms                                            |
| `math.ceil(x)` / `math.floor(x)` | O(1)            | O(1)               | Round up / down to nearest int                        |
| `math.pow(x, y)`            | O(1)                | O(1)               | Float power (use `**` for exact integer power)        |

### Examples

```python
import math

# Infinity as a sentinel
best = math.inf
for x in [5, 2, 8, 1]:
    best = min(best, x)
print(best)                   # 1

# GCD / LCM
print(math.gcd(12, 18))       # 6
print(math.gcd(12, 18, 24))   # 6  (multiple args, 3.9+)
print(math.lcm(4, 6))         # 12

# Exact integer square root — safer than int(n ** 0.5) for large n
print(math.isqrt(17))         # 4
print(math.isqrt(10**18))     # exact, no float rounding issues

# Combinatorics
print(math.factorial(5))      # 120
print(math.comb(5, 2))        # 10  (5 choose 2)
print(math.perm(5, 2))        # 20  (5 permute 2)

# Rounding & logs
print(math.ceil(4.2), math.floor(4.8))   # 5 4
print(math.log2(8))                       # 3.0
```

---

## sortedcontainers.SortedList

<a id="sortedcontainers">sortedcontainers.SortedList</a>

### When to Use

- True **O(log n)** insert/remove/index lookup on a sorted sequence — `list` + `bisect` is only O(log n) for the *search*, the actual insert/delete is still O(n) because it shifts array elements
- Sliding window median, k-th smallest in a stream, range-count queries, "maintain sorted order under online insertions"

> **Note**: Not in the standard library — requires `pip install sortedcontainers`. It **is** preinstalled in LeetCode's judge, so it's safe to rely on there.

### Declaration

```python
from sortedcontainers import SortedList, SortedDict, SortedSet
sl = SortedList()
sl = SortedList([5, 3, 1, 4])
```

### Properties and Methods

| Method / Operation                  | Time Complexity | Space Complexity | Description                                  |
| ------------------------------------ | --------------- | ----------------- | --------------------------------------------- |
| `sl.add(x)`                          | O(log n)         | O(1)               | Insert maintaining sort order                 |
| `sl.remove(x)`                       | O(log n)         | O(1)               | Remove first occurrence by value (raises if missing) |
| `sl.discard(x)`                      | O(log n)         | O(1)               | Remove if present, no error if missing        |
| `sl.pop(i)`                          | O(log n)         | O(1)               | Remove and return element at index i          |
| `sl[i]`                              | O(log n)         | O(1)               | Access by index                               |
| `sl.index(x)`                        | O(log n)         | O(1)               | Index of value                                |
| `sl.bisect_left(x)` / `bisect_right(x)` | O(log n)      | O(1)               | Binary search boundaries (same semantics as `bisect`) |
| `sl.count(x)`                        | O(log n)         | O(1)               | Count occurrences                             |
| `x in sl`                            | O(log n)         | O(1)               | Membership test                               |
| `len(sl)`                            | O(1)             | O(1)               | Number of elements                            |

### Examples

```python
from sortedcontainers import SortedList

sl = SortedList([5, 1, 3])
sl.add(4)
print(sl)                  # SortedList([1, 3, 4, 5])

sl.remove(3)
print(sl)                  # SortedList([1, 4, 5])

print(sl[0], sl[-1])       # 1 5  (smallest, largest in O(log n))
print(sl.bisect_left(4))   # 1

# Sliding window median (k-sized window)
def median_sliding_window(nums, k):
    window = SortedList()
    result = []
    for i, x in enumerate(nums):
        window.add(x)
        if len(window) > k:
            window.remove(nums[i - k])
        if len(window) == k:
            mid = k // 2
            if k % 2:
                result.append(float(window[mid]))
            else:
                result.append((window[mid - 1] + window[mid]) / 2)
    return result

print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

---

## Union-Find (Disjoint Set Union)

<a id="unionfind">Union-Find (Disjoint Set Union)</a>

### When to Use

- **Not built into Python** — implement as a small class
- Connected components / cycle detection in undirected graphs
- Kruskal's MST, "number of provinces", "redundant connection", "accounts merge" style problems

### Declaration

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False                  # already connected
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

### Properties and Methods

| Method / Operation   | Time Complexity      | Space Complexity | Description                                         |
| --------------------- | --------------------- | ----------------- | ----------------------------------------------------- |
| `uf.find(x)`          | O(α(n)) amortized     | O(1)               | Find root, with path compression                      |
| `uf.union(x, y)`      | O(α(n)) amortized     | O(1)               | Merge two sets, with union by rank                     |

> α(n) is the inverse Ackermann function — effectively O(1) in practice for any realistic n.

### Examples

```python
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))   # True  — same component
print(uf.find(0) == uf.find(3))   # False

# Count connected components
def count_components(n, edges):
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a, b)
    return len({uf.find(i) for i in range(n)})

print(count_components(5, [[0, 1], [1, 2], [3, 4]]))   # 2

# Cycle detection in an undirected graph
def has_cycle(n, edges):
    uf = UnionFind(n)
    for a, b in edges:
        if not uf.union(a, b):    # union returns False if already connected
            return True
    return False

print(has_cycle(3, [[0, 1], [1, 2], [2, 0]]))   # True
```

---

## Trie

<a id="trie">Trie</a>

### When to Use

- **Not built into Python** — implement as a small class
- Prefix matching, autocomplete, word search, "longest common prefix", word dictionary with wildcard search

### Declaration

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

### Properties and Methods

| Method / Operation         | Time Complexity | Space Complexity | Description                          |
| ---------------------------- | --------------- | ----------------- | -------------------------------------- |
| `trie.insert(word)`          | O(L)             | O(L)               | L = length of word                     |
| `trie.search(word)`          | O(L)             | O(1)               | Exact word match                       |
| `trie.starts_with(prefix)`   | O(L)             | O(1)               | Prefix existence check                 |

### Examples

```python
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))        # True
print(trie.search("app"))          # False — "app" was never inserted as a full word
print(trie.starts_with("app"))     # True

trie.insert("app")
print(trie.search("app"))          # True
```

---

## LeetCode Boilerplate (ListNode / TreeNode)

<a id="boilerplate">LeetCode Boilerplate (ListNode / TreeNode)</a>

### When to Use

- LeetCode hands you these exact class definitions in linked-list and binary-tree problems — keep them memorized so you can build test inputs quickly without re-reading the problem's starter code

### Declaration

```python
# Singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Examples

```python
# Build a linked list: 1 -> 2 -> 3
head = ListNode(1, ListNode(2, ListNode(3)))

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

print_list(head)   # [1, 2, 3]

# Build a tree:
#      1
#     / \
#    2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))

def inorder(node, out=None):
    if out is None:
        out = []
    if node:
        inorder(node.left, out)
        out.append(node.val)
        inorder(node.right, out)
    return out

print(inorder(root))   # [2, 1, 3]
```

---

## Quick Reference Summary

### Time Complexity Comparison

| Operation         | list       | tuple      | dict      | set       | deque    | heapq     |
| ----------------- | ---------- | ---------- | --------- | --------- | -------- | --------- |
| Access by index   | O(1)       | O(1)       | —         | —         | O(n)*    | —         |
| Access first/last | O(1)       | O(1)       | —         | —         | O(1)     | O(1)      |
| Access by key     | —          | —          | O(1) avg  | —         | —        | —         |
| Add to end        | O(1) †     | —          | O(1) avg  | O(1) avg  | O(1)     | O(log n)  |
| Add to front      | O(n)       | —          | —         | —         | O(1)     | —         |
| Remove from end   | O(1)       | —          | —         | —         | O(1)     | —         |
| Remove from front | O(n)       | —          | —         | —         | O(1)     | —         |
| Remove by value   | O(n)       | —          | O(1) avg  | O(1) avg  | O(n)     | —         |
| Insert at middle  | O(n)       | —          | —         | —         | O(n)     | —         |
| Membership test   | O(n)       | O(n)       | O(1) avg  | O(1) avg  | O(n)     | O(n)      |
| Sort              | O(n log n) | O(n log n) | —         | —         | —        | O(n) ‡   |
| Pop minimum       | —          | —          | —         | —         | —        | O(log n)  |

\* O(1) for `deque[0]` and `deque[-1]`  
† Amortized  
‡ `heapify` is O(n); each subsequent `heappop` is O(log n)

### Space Complexity

All data structures: **O(n)** where n is the number of stored elements.  
`array.array` uses approximately **2× less** memory than `list` for numeric data.

### When to Use What

| Structure              | Use When                                                                        |
| ---------------------- | ------------------------------------------------------------------------------- |
| **list**               | Default ordered collection; fast end append/pop; random access by index         |
| **tuple**              | Immutable fixed sequence; function multi-return; dict keys; slight speed edge   |
| **str**                | Text data — remember it's immutable; use `''.join()` instead of `+=` in loops  |
| **dict**               | Key-value mapping; frequency counting; caching; any lookup table                |
| **set**                | Unique elements; fast membership test; set algebra (union, intersection, etc.)  |
| **frozenset**          | Hashable, immutable set; usable as a dict key or in another set                 |
| **deque**              | Queue (FIFO) or stack (LIFO); BFS; sliding window; any both-ends fast access    |
| **defaultdict**        | dict with auto-defaults; grouping items; building adjacency lists               |
| **Counter**            | Frequency counting; most-common queries; multiset arithmetic; anagram check     |
| **OrderedDict**        | LRU cache (`move_to_end`); reordering keys; pre-Python 3.7 ordered dict        |
| **namedtuple**         | Lightweight immutable records with named fields; readable CSV rows              |
| **heapq**              | Priority queue; K-th smallest/largest; Dijkstra's; merging sorted iterables    |
| **bisect**             | Binary search on sorted list; sorted insertion; range/boundary queries          |
| **array.array**        | Large memory-efficient arrays of uniform numeric type                           |
| **functools.lru_cache**| Memoizing recursive functions; top-down DP                                      |
| **math**               | Infinity sentinels, GCD/LCM, exact integer sqrt, combinatorics                  |
| **sortedcontainers.SortedList** | True O(log n) sorted insert/remove; sliding window median, k-th in a stream |
| **Union-Find**         | Connected components; cycle detection; Kruskal's MST (not built-in)             |
| **Trie**               | Prefix matching; autocomplete; word search (not built-in)                       |

---

## Additional Tips

### String Building (StringBuilder Equivalent)

```python
# ❌ SLOW — string += allocates a new string every iteration: O(n²) total
result = ""
for i in range(1000):
    result += str(i)

# ✅ FAST — collect in list, join once: O(n) total
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)

# Even more concise with a generator
result = "".join(str(i) for i in range(1000))
```

### Common Built-in Functions (Work on Most Iterables)

```python
# Sorting with key
data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted(data, key=lambda x: x[1])                       # sort by second element
sorted(data, key=lambda x: x[0], reverse=True)         # sort by first, descending

# Multiple sort keys (sort by grade descending, then name ascending)
students = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
sorted(students, key=lambda s: (-s[1], s[0]))
# → [('Alice', 90), ('Charlie', 90), ('Bob', 85)]

# zip
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
d = dict(zip(keys, vals))   # {'a': 1, 'b': 2, 'c': 3}

# enumerate (start index can be customised)
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(i, val)   # 1 a / 2 b / 3 c

# map and filter (usually prefer comprehensions)
doubled = list(map(lambda x: x * 2, [1, 2, 3]))          # [2, 4, 6]
evens   = list(filter(lambda x: x % 2 == 0, range(10)))  # [0, 2, 4, 6, 8]

# any / all — short-circuit
print(any(x > 5 for x in [1, 2, 3]))    # False
print(all(x > 0 for x in [1, 2, 3]))    # True

# min / max with key
words = ["apple", "banana", "kiwi"]
print(min(words, key=len))    # kiwi
print(max(words, key=len))    # banana

# sum with generator expression
print(sum(x**2 for x in range(5)))   # 30
```

### Comprehensions

```python
# List comprehension
[expr for item in iterable if condition]

# Dict comprehension
{k: v for k, v in iterable if condition}

# Set comprehension
{expr for item in iterable}

# Generator expression — lazy, memory-efficient
(expr for item in iterable)

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]   # [1, 2, 3, 4, 5, 6]

# Transpose a matrix
transposed = [[row[i] for row in matrix] for i in range(2)]
# [[1, 3, 5], [2, 4, 6]]

# Conditional expression (ternary)
lst = [x if x % 2 == 0 else -x for x in range(8)]
# [0, -1, 2, -3, 4, -5, 6, -7]
```

### Useful itertools

```python
import itertools

# Combinations and permutations
list(itertools.combinations([1, 2, 3], 2))     # [(1,2),(1,3),(2,3)]
list(itertools.permutations([1, 2, 3], 2))     # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
list(itertools.combinations_with_replacement([1,2], 2))  # [(1,1),(1,2),(2,2)]

# Chain — flatten iterables without copying
list(itertools.chain([1, 2], [3, 4], [5]))     # [1, 2, 3, 4, 5]

# Product — Cartesian product
list(itertools.product([0, 1], repeat=2))      # [(0,0),(0,1),(1,0),(1,1)]

# groupby — sort first!
from itertools import groupby
data = sorted([("a", 1), ("b", 2), ("a", 3)], key=lambda x: x[0])
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 3)]
# b [('b', 2)]

# accumulate — prefix sums / running totals
list(itertools.accumulate([1, 2, 3, 4]))       # [1, 3, 6, 10]
import operator
list(itertools.accumulate([1,2,3,4], operator.mul))  # [1,2,6,24] (factorial)

# islice — slice an iterator without materialising it
first5 = list(itertools.islice(iter(range(100)), 5))   # [0, 1, 2, 3, 4]
```

### Copying Pitfalls

```python
import copy

lst = [[1, 2], [3, 4]]

# Shallow copy — outer list is copied, inner lists are SHARED
shallow = lst.copy()        # same as lst[:]  or  list(lst)
shallow[0].append(99)
print(lst)     # [[1, 2, 99], [3, 4]]  ← MUTATED — unexpected!

# Deep copy — fully independent at every level
deep = copy.deepcopy(lst)
deep[0].append(99)
print(lst)     # [[1, 2, 99], [3, 4]]  ← unchanged
```

---

### Bit Manipulation Cheatsheet

```python
x = 12   # 0b1100
i = 2

# Check bit i
(x >> i) & 1

# Set bit i
x | (1 << i)

# Clear bit i
x & ~(1 << i)

# Toggle bit i
x ^ (1 << i)

# Drop the lowest set bit
x & (x - 1)

# Isolate the lowest set bit
x & (-x)

# Count set bits (Hamming weight)
bin(x).count('1')      # works everywhere
x.bit_count()           # Python 3.10+, faster

# Check power of two (x > 0 required)
x > 0 and (x & (x - 1)) == 0

# XOR swap (no temp variable)
a, b = 5, 9
a ^= b
b ^= a
a ^= b
print(a, b)             # 9 5

# Classic: find the single number that appears once, rest appear twice
nums = [4, 1, 2, 1, 2]
result = 0
for n in nums:
    result ^= n
print(result)           # 4
```

### 2D List Initialization Pitfall

```python
# ❌ WRONG — all rows reference the SAME inner list object
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)   # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  ← every row changed!

# ✅ CORRECT — each row is its own independent list
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print(grid)   # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### Recursion Limit

```python
import sys
sys.setrecursionlimit(10000)   # default is ~1000 — raise it for deep DFS / recursive DP

# Still bounded by the actual call stack — very deep recursion (100k+ frames)
# can still crash with a segfault. For graphs/trees that might be very deep
# (e.g. a skewed binary tree or long linked list), prefer an iterative
# approach with an explicit stack/queue instead of raising the limit blindly.
```

---

> **Note**: All hash-based complexities (`dict`, `set`, `Counter`, `defaultdict`) are **average case O(1)**. Worst case can degrade to O(n) with hash collisions, but Python's randomised hash seed (SipHash) makes this extremely rare in practice.

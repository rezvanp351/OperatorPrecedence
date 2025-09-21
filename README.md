# Operator Precedence in Python

This README explains the operator precedence (which operators are evaluated first) in Python. It is designed for placement in a GitHub repository and for learners who want clear examples and explanations.

### Quick Overview
Operators in Python have different precedence levels. An operator with higher precedence is evaluated before operators with lower precedence, unless parentheses alter the order.

**Precedence — highest to lowest:**

1. `()` — Parentheses
2. `**` — Exponentiation (right-associative)
3. `+x, -x, ~x` — Unary plus, unary minus, bitwise NOT
4. `*  /  //  %` — Multiplication, division, floor division, modulus
5. `+  -` — Addition and subtraction
6. `<<  >>` — Bitwise left and right shifts
7. `&` — Bitwise AND
8. `^` — Bitwise XOR
9. `|` — Bitwise OR
10. `==  !=  >  >=  <  <=  is  is not  in  not in` — Comparisons, identity, membership
11. `not` — Logical NOT
12. `and` — Logical AND
13. `or` — Logical OR

**Notes:**
- `**` is right-associative: `2 ** 3 ** 2` means `2 ** (3 ** 2)`.
- Most other binary operators are left-associative (evaluated left-to-right).

---

## Detailed Level-by-Level Explanation with Examples

### 1) Parentheses `()`
Parentheses always evaluate first and can be used to change the natural order of evaluation.

```py
(2 + 3) * 4  # 20
2 + 3 * 4    # 14 (without parentheses)
```

### 2) Exponentiation `**` (right-associative)

```py
2 ** 3 ** 2  # 2 ** (3 ** 2) = 2 ** 9 = 512
```

Important interaction with unary minus:

```py
-3 ** 2     # = -(3 ** 2) = -9
(-3) ** 2   # = 9
```

If you want the negative value to be exponentiated, use parentheses.

### 3) Unary operators `+x, -x, ~x`

```py
x = 5
+ x    # 5
- x    # -5
~ x    # bitwise NOT; ~5 = -6 in two's complement
```

`~n` equals `-(n + 1)`.

### 4) `* / // %` (multiplication, division, floor division, modulus)

```py
6 / 3 * 2   # (6 / 3) * 2 = 4.0
7 // 2      # 3  (floor division)
7 % 3       # 1  (modulus)
```

These operators are evaluated left-to-right.

### 5) `+ -` (addition and subtraction)

```py
5 + 2 - 3   # (5 + 2) - 3 = 4
```

### 6) Bitwise shifts `<< >>`

```py
1 << 3    # 8
8 >> 2    # 2
```

### 7) Bitwise AND `&`

```py
5 & 3   # 1  (0b101 & 0b011 = 0b001)
```

### 8) Bitwise XOR `^`

```py
5 ^ 3   # 6  (0b101 ^ 0b011 = 0b110)
```

### 9) Bitwise OR `|`

```py
5 | 3   # 7  (0b101 | 0b011 = 0b111)
```

### 10) Comparisons, identity, membership

```py
3 < 4           # True
3 == 4          # False
'a' in 'cat'    # True
x is None       # depends on x

# Chained comparisons
1 < 2 < 3        # True
```

Comparison chaining behaves like `(1 < 2) and (2 < 3)` but is evaluated more efficiently.

### 11) `not` (logical NOT)

```py
not True   # False
not 0      # True  (0 is falsy)
```

### 12) `and` (logical AND)

```py
True and False   # False
1 and 2          # 2  (returns the last evaluated operand)
```

`and` short-circuits: if the left operand is falsy, the right operand is not evaluated.

### 13) `or` (logical OR)

```py
True or False    # True
0 or 5           # 5  (returns the first truthy operand)
```

`or` also short-circuits: if the left operand is truthy, the right operand is not evaluated.

---

## Step-by-step Example

Consider the expression:

```py
expr = 2 + 3 * 4 ** 2 // (1 + 1) - -5
```

Evaluation order:
1. Parentheses: `(1 + 1)` → `2`
2. Exponentiation: `4 ** 2` → `16`
3. Multiplication: `3 * 16` → `48`
4. Floor division: `48 // 2` → `24`
5. Addition: `2 + 24` → `26`
6. Double unary minus: `- -5` → `+5`
7. Final: `26 - -5` → `31`

So `expr == 31`.

---

## Common Gotchas
- `-3 ** 2` is `-9`, not `9`. Use `(-3) ** 2` if you want the square of -3.
- `2 ** 3 ** 2` is `512` because exponentiation is right-associative.
- Logical operators (`and`, `or`) return one of their operands, not just `True`/`False`.
- Use parentheses to make complex expressions clear and avoid mistakes.

---

## How to use these files in your GitHub repo
- Save the README portion as `README.md` in the repository root.
- Save the example code as `examples.py` and include it in the repo. Users can run it to see outputs.

---

## Suggested tags / hashtags for a video or repo
`#Python #PythonTips #OperatorPrecedence #Programming #LearnPython #Python3`

---

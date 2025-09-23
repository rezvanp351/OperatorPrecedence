a = 5
b = 2
c = [1, 2, 3, 4, 5]

# Main expression
result = (a + b) * 2 ** b - +a // b % 2 << 1 | (a ^ b & 3) > 4 and not (a is b or a in c)

print(result)

"""
Step-by-step explanation of operator precedence:

1. Parentheses () 
   (a + b) = 7
   (b & 3) = 2, then (a ^ 2) = 7
   (a is b or a in c) → False or True = True

2. Exponentiation ** 
   2 ** b = 2 ** 2 = 4

3. Unary +  
   +a = 5

4. Multiplication, Floor Division, Modulus (* // %)  
   (7 * 4) = 28
   (5 // 2) = 2
   (2 % 2) = 0

5. Addition and Subtraction (+ -)  
   28 - 0 = 28

6. Bitwise shifts (<< >>)  
   28 << 1 = 56

7. Bitwise AND, XOR, OR (& ^ |)  
   From parentheses: (a ^ (b & 3)) = 7
   Then (56 | 7) = 63

8. Comparisons (== != > >= < <= is is not in not in)  
   (63 > 4) = True

9. Logical NOT (not)  
   not(True) = False   ← from the last parentheses

10. Logical AND (and)  
   True and False = False

Final Result = False
"""

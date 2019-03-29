# Theory of Computation Sprint Challenge

## Computation

Fill out truth tables for the following expressions:

1. `(A ∨ ¬B)`   (alternate: `(A || !B)`)
```
A     B     result
-------------------
0     0       1
0     1       0
1     0       1
1     1       1
```

2. `(¬A ∨ B) ∧ ¬(A ∧ ¬B)`   (alternate: `(!A || B) && !(A && !B)`)
```
A     B     result
-------------------
0     0       1
0     1       1
1     0       0
1     1       1
```

3. `¬(A ∨ B) ∨ ( (A ∨ C) ∧ ¬(B ∨ ¬C) )`   (alternate: `!(A || B) || ( (A || C) && !(B || !C) )`)
  * (Hint: Is it possible to calculate this using code? Yes, see below for truthtable.py output)
```
A     B     C     result
-------------------------
0     0     0       1
0     0     1       1
0     1     0       0
0     1     1       0
1     0     0       0
1     0     1       1
1     1     0       0
1     1     1       0
```
<!-- 
A: False B: False C: False ---- True
A: False B: False C: True ---- True
A: False B: True C: False ---- False
A: False B: True C: True ---- False
A: True B: False C: False ---- False
A: True B: False C: True ---- True
A: True B: True C: False ---- False
A: True B: True C: True ---- False 
-->

## STRETCH GOAL

The sum of two binary digits can be represented with the following truth table:
CARRY - AND; SUM - XOR
* A + B
```
A     B     CARRY   SUM
------------------------
0     0       0      0
0     1       0      1
1     0       0      1
1     1       1      0
```
This can be represented with boolean algebra like so:

* `SUM = A ⊕ B`  (alternate: `A ^ B` or `A xor B`)
* `CARRY = A ∧ B`  (alternate: `A && B`)


How can you represent the SUM and CARRY of adding THREE digits with a truth table and in boolean algebra?

* A + B + C
```
A     B     C      carry   sum
--------------------------------
0     0     0        0      0
0     0     1        0      1
0     1     0        0      1
0     1     1        0      0
1     0     0        0      1
1     0     1        0      0
1     1     0        0      0
1     1     1        1      1
```
* SUM = `A ⊕ B ⊕ C`  (alternate: `A ^ B ^ C` or `A xor B xor C`)
* CARRY = `A ∧ B ∧ C`  (alternate: `A && B && C`)


*1. Striver_a2z_sheet/step1/lec2/pattern11.py*
pattern 
```text
1
0 1
1 0 1
```
**Intuition**: Use two loops—outer for rows and inner for alternating binary values. Determine the starting value for each row (`1` for odd, `0` for even) and toggle using XOR (`start ^= 1`).

```python

    for i in range(1, n+1):
        start: int = i % 2

        for j in range(i):
            print(start, end=' ')
            start ^= 1
        print()
```
---
*2. Striver_a2z_sheet/step1/lec2/pattern12.py*
```text
1         1
1 2     2 1
1 2 3 3 2 1
```
The pattern can be broken into three parts for each row:
- Left Part: Numbers increment from 1 to the row number (i).
- Spaces: Decreasing spaces between the left and right parts, calculated dynamically based on the row.
- Right Part: Numbers decrement from the row number (i) to 1.
```python
def numberCrown(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1): # first pattern
            print(j, end=" ")
        # for k in range()
        for k in range(2*(n-i)): # space pattern
            print(' ',end="")
        for l in range(i,0,-1):
            print(l, end=" ")
        print()
```
---
*3. Striver_a2z_sheet/step1/lec2/pattern14.py*

```text
A
A B
A B C
```

 **Intuition**: In python we cant add ints to str variable. Here we will need tp use in built function `chr` and `ord` to convert ASCII value to str and str to ASCII value respectively.

```python
    for i in range(1, n+1):
        val = 'A'
        for j in range(1,i+1):
            print(val, end =" ")
            val = chr(ord(val) + 1)
        print()
```





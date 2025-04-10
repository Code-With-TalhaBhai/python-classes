
### Divide(Right-Shift):
```
n = (n / 2) -> Dividing by Decimal Operators
n = n >> 1 == n/2 -> Dividing by bitwise Operators
```
In bitwise, division works for only 2 ^ k, it means (x/2,x/4,x/8,x/16)->(x/2^1,x/2^2,x/2^3,x/2^4)----->(Here, ^ refers to power)
```
x / 2 ===== x >> 1 
x / 4 ===== x >> 2 
x / 8 ===== x >> 3 
x / 2 ^ k ====== x >> k
```

### Multiply(Left-Shift)
```
n = n * 2
n = n << 1
```


### Square:
Number which is square of 2(16,8,32) has only one set-bit (1000,100,10000). And, the prev number before square(15,7,31) has all set-bits(111,1111,1111). The square of n is equal to 1 << n. <br>
``` 
2 ** n == 1 << n 
```
To check number is square of 2 i.e
```
x & x - 1 == 0 (doesn't work if the x = 0 which is edge case)
``` 



### Consecutive-numbers:
Two Consecutive numbers must have change in their position of last set-bit. And when we perform `AND` operation on `n` and `n-1` (n & n-1). It decreases the set-bit count by 1.
```
n & n - 1
```

### XOR
XOR of two same numbers are always zero.


### Even or Odd
If the rightmost bit corresponds to 1, it means numbers is odd. If it is 0 it means number is even.
```
(x % 2 == 1) -> (x & 1 == 1) -> odd
(x % 2 == 0) -> (x & 1 == 0)  -> even
```

### Check ith-bit
To check ith-bit is set or not.
```
x & (1 << i)
```

### Set ith-bit
To set ith-bit we perform
```
x | (1 << i)
```

### Clear ith-bit
To clear ith-bit we perform
```
x & ~(1 << i)
```

### Toggle ith-bit
To perform toggle on ith-bit
```
x ^ (1 << i)
```


### Modulus
If we want to take modulus of number with 2 ^ n. Then, it could be done by:

```
x = x % n ----> n should be power of 2 i,e, n ^ 2
x = x & (n - 1)
```


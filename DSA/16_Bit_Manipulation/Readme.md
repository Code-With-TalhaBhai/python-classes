
#### Divide:
n = (n / 2) -> decimal
n = n >> 1 == n/2 -> binary


#### Square:
Number which is square of 2(16,8,32) has only one set-bit. And, the prev number before square(15,7,31) has all set-bits


#### Consecutive-numbers:
Two Consecutive numbers must have change in their position of last set-bit. And when we perform `AND` operation on `n` and `n-1` (n & n-1). It decreases the set-bit count by 1.


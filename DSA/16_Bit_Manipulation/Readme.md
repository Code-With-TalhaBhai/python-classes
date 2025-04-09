
### Divide:
`n = (n / 2) -> decimal` <br>
`n = n >> 1 == n/2 -> binary`


### Square:
Number which is square of 2(16,8,32) has only one set-bit (1000,100,10000). And, the prev number before square(15,7,31) has all set-bits(111,1111,1111). The square of n is equal to 1 << n. <br>
` 2 ** n == 1 << n ` <br>
To check number is square of 2 i.e <br>
`x & x - 1 == 0` (doesn't work if the x = 0 which is edge case)



### Consecutive-numbers:
Two Consecutive numbers must have change in their position of last set-bit. And when we perform `AND` operation on `n` and `n-1` (n & n-1). It decreases the set-bit count by 1.


### XOR
XOR of two same numbers are always zero.


### Even or Odd
If the rightmost bit corresponds to 1, it means numbers is odd. If it is 0 it means number is even. <br>
`(x % 2 == 1) -> (x & 1 == 1)` -> odd <br>
`(x % 2 == 0) -> (x & 1 == 0)` -> even


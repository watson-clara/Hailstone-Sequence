# Hailstone Sequence

## Author
**Clara Watson**

## Background
A hailstone sequence starts with some positive integer. If that integer is even, then you divide it by two to get the next integer in the sequence, but if it is odd, then you multiply it by three and add one to get the next integer in the sequence. Then you use the value you just generated to find the next value, according to the same rules.  For example, if our initial number is 3, the subsequent numbers will be: 10, 5, 16, 8, 4, 2, 1.

## Program Description
This program takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1. If the starting integer is 1, the return value should be 0, since it takes no steps to reach 1 . For example, if the starting integer is 3, then the sequence would go: 3, 10, 5, 16, 8, 4, 2, 1, and the return value should be 7, since it took 7 steps to reach 1. Your function does not need to print anything out - just return a value.



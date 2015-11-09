{-
A. Candy Bags
==============
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Gerald has n younger brothers and their number happens to be even. One day he bought n^2 candy bags. One bag has one candy, one bag has two candies, one bag has three candies and so on. In fact, for each integer k from 1 to n^2 he has exactly one bag with k candies.

Help him give n bags of candies to each brother so that all brothers got the same number of candies.

Input
-----
The single line contains a single integer n (n is even, 2 ≤ n ≤ 100) — the number of Gerald's brothers.

Output
------
Let's assume that Gerald indexes his brothers with numbers from 1 to n. You need to print n lines, on the i-th line print n integers — the numbers of candies in the bags for the i-th brother. Naturally, all these numbers should be distinct and be within limits from 1 to n^2. You can print the numbers in the lines in any order.

It is guaranteed that the solution exists at the given limits.

Sample test(s)
--------------
input
```
2
```
output
```
1 4
2 3
```

Note
-----
The sample shows Gerald's actions if he has two brothers. In this case, his bags contain 1, 2, 3 and 4 candies. He can give the bags with 1 and 4 candies to one brother and the bags with 2 and 3 to the other brother.
-}

main = do
  input <- getContents
  let n = read input
  mapM_ (putStrLn . unwords . map show) $ candyDistribute n 
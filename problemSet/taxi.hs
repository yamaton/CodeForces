{-
B. Taxi
=======
time limit per test 3 seconds
memory limit per test 256 megabytes
input standard input
output standard output

After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus to celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to go to Polycarpus together. They decided to get there by taxi. Each car can carry at most four passengers. What minimum number of cars will the children need if all members of each group should ride in the same taxi (but one taxi can take more than one group)?

Input
------
The first line contains integer n (1 ≤ n ≤ 10^  5) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.

Output
-------
Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.

Sample test(s)
--------------
input
```
5
1 2 4 3 3
```
output
```
4
```
input
```
8
2 3 4 4 2 1 3 1
```
output
```
5
```
Note
In the first test we can sort the children into four cars like this:

- the third group (consisting of four children),
- the fourth group (consisting of three children),
- the fifth group (consisting of three children),
- the first and the second group (consisting of one and two children, correspondingly).
There are other ways to sort the groups into four cars.
-}

import Data.List (sort, group)

count :: Int -> [Int] -> Int
count k xs = length $ filter (== k) xs

taxiNumber :: [Int] -> Int
taxiNumber xs = n4 + n3 + ceiling (fromIntegral n2 / 2) + adjust
  where [n1, n2, n3, n4]  = map (`count` xs) [1,2,3,4]
        adjust = max 0 $ ceiling $ (fromIntegral (n1 - n3 - 2 * (n2 `mod` 2))) / 4 

reader :: String -> [Int]
reader s = map read $ words second
  where [_, second] = lines s

main = do
  input <- getContents
  let xs = reader input
  print $ taxiNumber xs

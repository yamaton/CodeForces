{-
A. Theatre Square
==================
time limit per test2 seconds
memory limit per test64 megabytes
inputstandard input
outputstandard output

Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

Input
-----
The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

Output
------
Write the needed number of flagstones.

Sample test(s)
--------------
input
```
6 6 4
```
output
```
4
```
-}

theatreSquare :: Integer -> Integer -> Integer -> Integer
theatreSquare n m a = ceiling (n' / a') * ceiling (m' / a')
  where [n', m', a'] = map fromIntegral [n, m, a]

main = do 
  input <- getLine
  let [n, m, a] = map read (words input)
  print $ theatreSquare n m a
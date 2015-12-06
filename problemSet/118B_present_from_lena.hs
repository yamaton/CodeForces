{-
B. Present from Lena
=====================
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vasya's birthday is approaching and Lena decided to sew a patterned handkerchief to him as a present. Lena chose digits from 0 to n as the pattern. The digits will form a rhombus. The largest digit n should be located in the centre. The digits should decrease as they approach the edges. For example, for n = 5 the handkerchief pattern should look like that:


          0
        0 1 0
      0 1 2 1 0
    0 1 2 3 2 1 0
  0 1 2 3 4 3 2 1 0
0 1 2 3 4 5 4 3 2 1 0
  0 1 2 3 4 3 2 1 0
    0 1 2 3 2 1 0
      0 1 2 1 0
        0 1 0
          0

Your task is to determine the way the handkerchief will look like by the given n.

Input
------
The first line contains the single integer n (2 ≤ n ≤ 9).

Output
------
Print a picture for the given n. You should strictly observe the number of spaces before the first digit on each line. Every two adjacent digits in the same line should be separated by exactly one space. There should be no spaces after the last digit at the end of each line.

Sample test(s)
---------------
input
2
output
    0
  0 1 0
0 1 2 1 0
  0 1 0
    0

input
3
output
      0
    0 1 0
  0 1 2 1 0
0 1 2 3 2 1 0
  0 1 2 1 0
    0 1 0
      0

-}
import Data.List (intercalate)

pattern :: Int -> [String]
pattern n = map helper (upAndDown n)
  where helper k = replicate (2 * (n - k)) ' ' ++ (intercalate " " . map show) (upAndDown k)

  
upAndDown :: Int -> [Int]
upAndDown 0 = [0]
upAndDown n = tmp ++ (tail . reverse) tmp
  where tmp = [0 .. n]

main = do 
  input <- getLine 
  let n = read input
  mapM_ putStrLn (pattern n)

{-
C. The Last Hole!
==================
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Luyi has n circles on the plane. The i-th circle is centered at (xi, yi). At the time zero circles start to grow simultaneously. In other words, the radius of each circle at time t (t > 0) is equal to t. The circles are drawn as black discs on an infinite white plane. So at each moment the plane consists of several black and white regions. Note that the circles may overlap while growing.


We define a hole as a closed, connected white region. For instance, the figure contains two holes shown by red border. During growing some holes may be created and it is easy to see that each created hole will disappear eventually. Luyi asks you to find moment of time such that the last hole disappears. In other words, you should find the first moment such that no hole can be seen after that.

Input
------
The first line of the input contains integer n (1 ≤ n ≤ 100). Each of the next n lines contains two integers xi and yi ( - 10^4 ≤ xi, yi ≤ 10^4), indicating the location of i-th circle.

It's guaranteed that no two circles are centered at the same point.

Output
------
Print the moment where the last hole disappears. If there exists no moment in which we can find holes print -1.

The answer will be considered correct if the absolute or relative error does not exceed 10^-4.

Sample test(s)
---------------
input
3
0 0
1 1
2 2
output
-1

input
4
0 0
0 2
2 2
2 0
output
1.414214

input
4
0 1
0 -1
-2 0
4 0
output
2.125000

-}


timeOfLastHoleDissapears :: [[Int]] -> Double
timeOfLastHoleDissapears 

main = do 
  input <- getContents
  let xs = [(map read . words) line | line <- tail . lines xs]



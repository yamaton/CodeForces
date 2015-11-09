{-
A. Lucky Division
==================
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

Input
------
The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.

Output
------
In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).

Sample test(s)
---------------
input
47
output
YES

input
16
output
YES

input
78
output
NO

-}
import Data.List (nub, sort, findIndices)
import Data.Map (toList, fromListWith)
import Control.Applicative ((<$>), (<*>))
import Control.Monad (when, forM_, replicateM)
import Data.Array.ST (newArray, readArray, writeArray, runSTUArray)
import Data.Array.Unboxed (UArray, assocs)

sieve :: Int -> UArray Int Bool
sieve n = runSTUArray $ do
    let maxP = floor . sqrt $ fromIntegral n
    sieveTF <- newArray (2, n) True 
    forM_ [2..maxP] $ \p -> do
      isPrime <- readArray sieveTF p
      when isPrime $ do
        forM_ [p*p, p*p+p .. n] $ \q -> do
          writeArray sieveTF q False
    return sieveTF

primesTo :: Int -> [Int]
primesTo n
  | n < 2     = []
  | otherwise = [i | (i,True) <- assocs $ sieve n]

cartesianProduct :: [[a]] -> [[a]]
cartesianProduct = foldr (\xs acc -> (:) <$> xs <*> acc) [[]]

tally :: Ord a => [a] -> [(a, Int)]
tally xs = toList $ fromListWith (+) [(x, 1)| x <- xs]

factorInteger :: Int -> [(Int, Int)]
factorInteger 0 = [(0, 1)]
factorInteger 1 = [(1, 1)]
factorInteger n = tally $ factor n
  where
    ps = (primesTo . round . sqrt . fromIntegral) n
    factor 1 = []
    factor p = k : factor (p `div` k)
      where 
        ds = dropWhile (\q -> p `mod` q /= 0) ps
        k = if null ds then p else head ds

divisors :: Int -> [Int]
divisors 1 = [1]
divisors n = sort [product xs | xs <- cartesianProduct factors]
  where factors = [ map (n^) [0..pow] | (n, pow) <- factorInteger n ]

---- 

isAlmostLucky :: Int -> Bool
isAlmostLucky x = isLucky x || 
                  ( (not . null) luckyDs && 
                    any (\k -> x `mod` k == 0) luckyDs )
  where luckyDs = filter isLucky $ divisors x

isLucky :: Int -> Bool
isLucky x = s == "47" || s == "4" || s == "7"
  where s = (sort . nub . show) x

boolToStr :: Bool -> String
boolToStr True = "YES"
boolToStr False = "NO"

main = do 
  input <- getLine
  let x = read input
  (putStrLn . boolToStr . isAlmostLucky) x


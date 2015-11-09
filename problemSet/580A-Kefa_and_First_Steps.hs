{-
Codeforces Round #321 (Div. 2)

Problem 580 A. Kefa and First Steps

@author yamaton
@date 2015-09-22
-}

import Control.Applicative
import Control.Monad
import Text.Printf
import System.IO (hPutStrLn, stderr)

import Data.List (maximumBy)
import Data.Ord (comparing)
-- import qualified Data.Map as Map
-- import qualified Data.Set as Set
-- import qualified Data.Foldable as F
-- import qualified Data.Traversable as T

-- lndcs : length of Longest Non-decreasing consecutive sequence
lndcs :: [Int] -> Int
lndcs xs = maximum $ scanl f 1 neighbors
  where
    f :: Int -> (Int, Int) -> Int
    f acc (a, b) | a <= b    = acc + 1
                 | otherwise = 1
    neighbors = zip xs (tail xs)


lndcs2 :: [Int] -> [Int]
lndcs2 [] = []
lndcs2 xs = maximumBy (comparing length) yss
  where
    yss = scanr g [last xs] neighbors
    g :: (Int, Int) -> [Int] -> [Int]
    g (a, b) acc | a <= b    = a:acc
                 | otherwise = [a]
    neighbors = zip xs (tail xs)


main :: IO ()
main = do
    n <- read <$> getLine :: IO Int
    xs <- (map read . words) <$> getLine :: IO [Int]
    let result = lndcs xs
    print result

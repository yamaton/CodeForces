{-
Codeforces

Problem

@author yamaton
@date 2015-09-22
-}

import Control.Applicative
import Control.Monad
import Text.Printf
import System.IO (hPutStrLn, stderr)
-- import qualified Data.Map as Map
-- import qualified Data.Set as Set
-- import qualified Data.Foldable as F
-- import qualified Data.Traversable as T

-- NOTE: ceiling (n / a) == floor ((n + a - 1) / a)
solve :: Integer -> Integer -> Integer -> Integer
solve n m a = ((n + a - 1) `div` a) * ((m + a - 1) `div` a)

main :: IO ()
main = do 
  [n, m, a] <- (map read . words) <$> getLine :: IO [Integer]
  let ans = solve n m a
  print ans

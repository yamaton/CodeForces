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

solve :: Int -> [Int] -> Int
solve = undefined


main :: IO ()
main = do
    n <- read <$> getLine :: IO Int
    xs <- (map read . words) <$> getLine :: IO [Int]
    -- ys <- replicateM n getLine
    let result = solve n xs
    print result

    hPutStrLn stderr $ printf "xs = %s" (show xs)
    hPutStrLn stderr $ printf "result = %d" result

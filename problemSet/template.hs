{-
Codeforces Round #332

Problem 599 B. Spongebob and Joke

@author yamaton
@date 2015-12-01
-}

import Control.Applicative
import Control.Monad
import Text.Printf (printf)
import qualified Data.ByteString.Char8 as B
import qualified System.IO as IO
import qualified Data.Map as M
import qualified Data.Set as S
-- import qualified Data.Foldable as F
-- import qualified Data.Traversable as T

solve :: Int -> [Int] -> Int
solve = undefined


main :: IO ()
main = do
    -- n <- read <$> getLine
    -- [n, m] <- (map read . words) <$> getLine :: IO [Int]
    -- xs <- (map read . words) <$> getLine :: IO [Int]
    n <- fst . fromJust . B.readInt <$> B.getLine
    fs <- map (fst . fromJust . B.readInt) . B.words <$> B.getLine
    bs <- map (fst . fromJust . B.readInt) . B.words <$> B.getLine
    ys <- replicateM n getLine
    let result = solve n xs
    print result

    -- IO.hPutStrLn IO.stderr $ printf "xs = %s" (show xs)
    -- IO.hPutStrLn IO.stderr $ printf "result = %d" result

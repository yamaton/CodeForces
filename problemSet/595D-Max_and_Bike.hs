{-
Codeforces Round #330 (Div. 2)

Problem 594 B / 595 D. Max and Bike

@author yamaton
@date 2015-11-10
-}

import System.Random
import Data.Fixed
import Control.Applicative
import Control.Monad
import Text.Printf
import System.IO (hPutStrLn, stderr)

-- import qualified Data.Map as Map
-- import qualified Data.Set as Set
-- import qualified Data.Foldable as F
-- import qualified Data.Traversable as T

randomSeq :: Int -> [Double]
randomSeq seed = randomRs (0, 1) (mkStdGen seed)

isDiffSmall :: (Double, Double) -> Bool
isDiffSmall (a, b) = diff < 1e-7 && diff / max (abs b)  1.0 < 1e-7
  where diff = abs (a - b)

fixOverShoot :: Double -> Double -> Double -> Double
fixOverShoot lb ub r x
  | lb < x < ub = x
  | otherwise   = lb + (ub - lb) * r

solve :: Int -> Int -> Int -> Double
solve r v d = snd . head $ filter isDiffSmall neighbors
  where
    r' = fromIntegral r
    v' = fromIntegral v
    d' = fromIntegral d
    estimate = d' / v'
    pm = if (d' / 2) `mod'` (2 * pi * r') < pi * r' then 1 else -1

    newton :: Double -> Double
    newton t = t - f t / dfdt t
    f :: Double -> Double
    f t = v' * t + 2 * pm * r' * sin (v' * t / (2 * r')) - d'
    dfdt :: Double -> Double
    dfdt t = v' * (1 + pm * cos (v' * t / 2 * r'))
    lb = -estimate
    ub = 10 * estimate
    rs = randoms 42
    series = scanl (\n r -> (newton . fixOverShoot lb ub r) n) estimate rs
    neighbors = zip series (tail series)


main :: IO ()
main = do
    [n, r, v] <- (map read . words) <$> getLine :: IO [Int]
    forM_ [1..n] $ \_ -> do
      [s, f] <- (map read . words) <$> getLine :: IO [Int]
      print (s, f)
      let d = f - s :: Int
      let result = solve r v d
      print result
      -- hPutStrLn stderr $ printf "d = %s" (show d)
      hPutStrLn stderr (printf "result = %.12f" result)

{-
Codeforces Round #327 (Div. 2)

Problem 591 C. Median Smoothing

@author yamaton
@date 2015-11-06
-}

import Data.List

alternatingPositionAndLength :: [Int] -> [(Int, Int)]
alternatingPositionAndLength = consecutiveHeadAndLength . alternatingIndices


-- excludes the first and last element
alternatingIndices :: [Int] -> [Int]
alternatingIndices [] = []
alternatingIndices [_] = []
alternatingIndices [_, _] = []
alternatingIndices (x:xs) = map (\(i, _, _) -> i) triples'
  where
    triples = zip3 [1..] (init (x:xs)) (init xs)
    triples' = filter (\(_, p, q) -> p == q) triples


consecutiveHeadAndLength :: [Int] -> [(Int, Int)]
consecutiveHeadAndLength [] = []
consecutiveHeadAndLength (x:xs) = helper 1 x xs
  where
    helper :: Int -> Int -> [Int] -> [(Int, Int)]
    helper i y [] = [(i, x)]
    helper i y (z:zs)
      | y + i == z = helper (i + 1) y zs
      | otherwise  = (i, x) : helper 1 z zs


segmentFinal :: [Int] -> [(Int, Int)] -> [(Int, Int)]
segmentFinal xs posLength = [f p l | (p, l) <- posLength]
  where
    f pos len
      | odd len   = replicate len v
      | otherwise = replicate (len `div` 2) v +
                    replicate (len `div` 2) (1 - v)
        where v = xs !! (pos - 1)


iterCount :: [(Int, Int)] -> Int
iterCount = max . map (`div` 2 . (+1) . snd)


solve :: [Int] -> [(Int, [Int])]
solve xs = undefined



main :: IO ()
main = do
  n <- read <$> getLine :: IO Int
  xs <- map read . words <$> getLine :: IO [Int]
  let (count, fixedPoint) = solve xs n
  print count
  print fixedPoint

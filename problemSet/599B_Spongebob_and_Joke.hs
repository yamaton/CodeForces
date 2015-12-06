{-
Codeforces Round #332

Problem 599 B. Spongebob and Joke

@author yamaton
@date 2015-12-01
-}


import Control.Applicative
import Control.Monad
-- import Text.Printf (printf)
import Data.Maybe (fromJust)
-- import qualified Data.Binary as Bin
import qualified Data.ByteString.Char8 as B
-- import qualified Data.ByteString.Lazy as BL
-- import qualified System.IO as IO
import qualified Data.Map.Strict as M
import qualified Data.Set as S


solve :: [Int] -> [Int] -> (String, [Int])
solve fs bs
  | any (`S.notMember` setFs) bs         = ("Impossible", [])
  | length ys /= S.size (S.fromList ys) = ("Ambiguity", [])
  | otherwise                           = ("Possible", recovered)
  where
    setFs = S.fromList fs
    setBs = S.fromList bs
    ys = filter (`S.member` setBs) fs
    invFsPairs = map (\(i, f) -> (f, i)) $ filter (\(_, f) -> f `S.member` setBs) (zip [1..] fs)
    invFsDict = M.fromList invFsPairs
    recovered = map (\i -> fromJust (M.lookup i invFsDict)) bs


main :: IO ()
main = do
    _ <- B.getLine
    fs <- map (fst . fromJust . B.readInt) . B.words <$> B.getLine
    bs <- map (fst . fromJust . B.readInt) . B.words <$> B.getLine
    let (msg, lst) = solve fs bs
    putStrLn msg
    if (null lst)
      then return ()
      -- else (B.putStrLn . B.unwords . map (BL.toStrict . Bin.encode)) lst
      else (putStrLn . unwords . map show) lst
    --
    -- IO.hPutStrLn IO.stderr $ printf "xs = %s" (show xs)
    -- IO.hPutStrLn IO.stderr $ printf "result = %d" msg

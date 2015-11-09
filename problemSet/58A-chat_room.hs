{-
58A. Chat room
==============
http://codeforces.com/problemset/problem/58/A
-}

---- Text.Regex.Posix is not available in Codeforces.com.

-- import Text.Regex.Posix ((=~))
-- isValidHello :: String -> Bool
-- isValidHello s = s /= "hello" && s =~ ".*h.*e.*l.*l.*o.*"


isValidHello :: String -> Bool
isValidHello = helper "hello"
  where
    helper :: String -> String -> Bool
    helper "" _ = True
    helper _ "" = False
    helper (c:cs) (x:xs)
      | c == x    = helper cs xs
      | otherwise = helper (c:cs) xs

boolToStr :: Bool -> String
boolToStr True = "YES"
boolToStr False = "NO"

main :: IO ()
main = do
  input <- getLine
  putStrLn $ (boolToStr . isValidHello) input

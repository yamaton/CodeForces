{-
A. String Task
================
time limit per test 2 seconds
memory limit per test 256 megabytes
input standard input
output standard output

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

Input
------
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Output
------
Print the resulting string. It is guaranteed that this string is not empty.

Sample test(s)
--------------
input
```
tour
```

output
```
.t.r
```

input
```
Codeforces
```
output
```
.c.d.f.r.c.s
```

input
```
aBAcAba
```
output
```
.b.c.b
```
-}

import Data.List (intersperse)
import Data.Char (toLower)

transform :: String -> String
transform s = if null t then t else '.':t
  where t = (intersperse '.' . filter (`notElem` "aeiouy") . map toLower) s

main = do 
  input <- getLine
  putStrLn $ transform input 

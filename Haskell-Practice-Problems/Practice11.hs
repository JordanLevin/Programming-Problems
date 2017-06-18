-- https://wiki.haskell.org/99_questions/11_to_20
import Practice1 ( myLast, mySecondLast, elementAt, myLength, myReverse, isPalindrome, myPack, myPackHelper, myCompress, myFlatten, encode)

-- Question 11
data Encoded a = Many Int a | One a deriving (Show)

encodeModified :: (Eq a) => [a] -> [Encoded a]
encodeModified x 
    | (myPackHelper x) == x = [Many (length x) (head x)]
    | length (myPackHelper x) == 1 = One (head x) : encodeModified (drop 1 x)
    | otherwise = Many (length (myPackHelper x)) (head (myPackHelper x)) : encodeModified (drop (length $ myPackHelper x) x)

-- Question 12
decodeHelper :: Encoded a -> [a]
decodeHelper (One x) = [x]
decodeHelper (Many 1 x) = [x]
decodeHelper (Many n x) = x : decodeHelper (Many (n-1) (x))

decodeModified :: [Encoded a] -> [a]
decodeModified [] = []
decodeModified (x:xs) = decodeHelper x ++ decodeModified xs

-- Question 13

-- Question 14
dupli :: [a] -> [a]
dupli [x] = [x, x]
dupli (x:xs) = [x, x] ++ dupli xs

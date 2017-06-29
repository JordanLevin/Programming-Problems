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

-- Question 15
repli :: [a] -> Int -> [a]
repli [] n = []
repli x 1 = x
repli [x] n = [x] ++ repli [x] (n-1)
repli (x:xs) n = (repli [x] n) ++ (repli xs n)

-- Question 16
-- Not working at the moment
{-dropOther :: [a] -> Int -> [a]-}
{-dropOther x 0 = []-}
{-dropOther x 1 = []-}
{-dropOther x n = dropHelper x n 0 []-}
{--- Helper function takes an additional int representing position in the list-}
{-dropHelper :: a -> Int -> Int -> a -> a-}
{-dropHelper x n count result-}
    {-| count == length x = result-}
    {-| count `mod` n /= 0 = (dropHelper x n (count+1) (result ++ x)) !! count-}
    {-| otherwise = dropHelper x n (count+1) result-}

-- Question 17
split :: [a] -> Int -> [a]
split list slice position = splitHelper list slice position []

splitHelper :: a -> Int -> Int -> a -> a
splitHelper list slice position accumulate
    | position < slice = (splitHelper list slice (position+1) accumulate) ++ (list !! position)
    | position == slice = accumulate


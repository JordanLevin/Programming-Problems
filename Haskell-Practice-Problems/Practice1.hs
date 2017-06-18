-- https://wiki.haskell.org/99_questions/1_to_10
module Practice1 ( myLast, mySecondLast, elementAt, myLength, myReverse, isPalindrome, myPack,
        myPackHelper, myCompress, myFlatten, encode) where


-- 1
myLast :: [a] -> a
myLast [] = error "nothing in list" 
myLast [x] = x
myLast (x:xs) = myLast xs 

-- 2
mySecondLast :: [a] -> a
mySecondLast [] = error "nothing in list" 
mySecondLast [x,y] = x
mySecondLast (x:xs) = mySecondLast xs 

-- 3
elementAt :: [a] -> Int -> a
elementAt [] x = error "nothing in list" 
elementAt (x:xs) 0 = x
elementAt (x:xs) y = elementAt xs (y-1)

-- 4
myLength :: [a] -> Integer
myLength (x:xs) = myLengthHelper xs 1

myLengthHelper :: [a] -> Integer -> Integer
myLengthHelper [] y = y 
myLengthHelper (x:xs) y = myLengthHelper xs (y+1)

-- 5
myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

-- 6
isPalindrome :: [Int] -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome (x:xs) = if x == last xs then isPalindrome (init xs) else False

--7
data NestedList a = Elem a | List [NestedList a]
myFlatten :: NestedList a -> [a]
myFlatten (List []) = []
myFlatten (Elem a) = [a]
myFlatten (List (x:xs)) = myFlatten x ++ (myFlatten (List xs))

-- 8
myCompress :: (Eq a) => [a] -> [a]
myCompress [x] = [x]
myCompress (x:xs)
    | head xs == x = myCompress xs
    | otherwise = x: myCompress xs

-- 9 
myPack :: (Eq a) => [a] -> [[a]]
myPack x 
    | (myPackHelper x) == x = [x]
    | otherwise = (myPackHelper x) : myPack (drop (length $ myPackHelper x) x)

myPackHelper :: (Eq a) => [a] -> [a]
myPackHelper [] = []
myPackHelper [x] = [x]
myPackHelper (x:xs)
    | head xs == x = x : myPackHelper xs
    | otherwise = [x]

-- 10
encode :: (Eq a) => [a] -> [(Int, a)]
encode x 
    | (myPackHelper x) == x = [(length x, head x)]
    | otherwise = (length (myPackHelper x), head (myPackHelper x)) : encode (drop (length $ myPackHelper x) x)

myLength :: [a] -> Integer
myLength (x:xs) = myLengthHelper xs 1

myLengthHelper :: [a] -> Integer -> Integer
myLengthHelper [] y = y 
myLengthHelper (x:xs) y = myLengthHelper xs (y+1)

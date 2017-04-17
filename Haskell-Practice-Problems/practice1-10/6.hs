isPalindrome :: [Int] -> Bool
isPalindrome [] = True
isPalindrome [x] = True
isPalindrome (x:xs) = if x == last xs then isPalindrome (init xs) else False

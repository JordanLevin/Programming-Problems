myLast :: [a] -> a
myLast [] = error "nothing in list" 
myLast [x] = x
myLast (x:xs) = myLast xs 

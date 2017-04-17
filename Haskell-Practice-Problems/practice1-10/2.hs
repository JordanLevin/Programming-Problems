mySecondLast :: [a] -> a
mySecondLast [] = error "nothing in list" 
mySecondLast [x,y] = x
mySecondLast (x:xs) = mySecondLast xs 

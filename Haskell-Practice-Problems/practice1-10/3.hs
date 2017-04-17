elementAt :: [a] -> Int -> a
elementAt [] x = error "nothing in list" 
elementAt (x:xs) 0 = x
elementAt (x:xs) y = elementAt xs (y-1)

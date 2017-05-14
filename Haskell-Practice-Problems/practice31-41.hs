
-- Problem 31
isPrime :: Int -> Bool
isPrime 2 = False
isPrime x
    | length (filter (== 0) (map (\z -> x `mod` z) nums)) > 0 = False
    | otherwise = True
    where nums = [2 .. round(sqrt (fromIntegral x))]

-- Problem 32
myGcd :: Int -> Int -> Int
myGcd x y
    | x == y = x
    | otherwise = myGcd (hi - lo) lo
    where 
        hi = max x y
        lo = min x y

-- Problem 33


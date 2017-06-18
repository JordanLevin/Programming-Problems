
-- Problem 31
isPrime :: Int -> Bool
isPrime 2 = True
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
coprime :: Int -> Int -> Bool
coprime x y = if myGcd x y == 1 then True else False

-- Problem 34
totient :: Int -> Int
totient x = length (filter (coprime x) [1..x])

-- Problem 35
primeFactors :: Int -> [Int]
primeFactors x
    | x == firstPrime x 2 = [x]
    | otherwise = firstPrime x 2 : primeFactors (x `div` firstPrime x 2)

firstPrime :: Int -> Int -> Int
firstPrime x y 
    | isPrime y && mod x y == 0 = y 
    | otherwise = firstPrime x (y+1)

-- Problem 36
primeFactorsMult :: Int -> [[Int]]
primeFactorsMult x
    |
    where
        factors = primeFactors x

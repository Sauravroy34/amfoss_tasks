isPrime :: Int -> Bool
isPrime n
    | n <= 1 = False
    | otherwise = all (\x -> n `mod` x /= 0) [2..isqrt n]
    where isqrt = floor . sqrt . fromIntegral

primeNumbersUpTo :: Int -> [Int]
primeNumbersUpTo n = filter isPrime [2..n]

main :: IO ()
main = do
    putStrLn "Enter a number (n):"
    n <- readLn
    putStrLn $ "Prime numbers up to " ++ show n ++ ":"
    let primes = primeNumbersUpTo n
    mapM_ (putStr . (++ " ") . show) primes
    putStrLn ""


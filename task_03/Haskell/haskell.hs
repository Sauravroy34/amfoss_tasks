check :: Int -> Bool
check 2 = True 
check n = all(\x -> n `mod` x /=0) [2..n-1]

give :: Int -> [Int]
give x = filter check [2..x]

main :: IO ()
main = do 
    putStrLn "enter a number"

    n <- readLn :: IO Int

    print(give n)

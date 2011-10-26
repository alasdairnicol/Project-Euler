-- Project Euler Problem 1
-- 
-- http://projecteuler.net/index.php?section=problems&id=1
-- 
-- If we list all the natural numbers below 10 that are multiples of 3
-- or 5, we -- get 3, 5, 6 and 9. The sum of these multiples is 23.
--
-- Find the sum of all the multiples of 3 or 5 below 1000.

main = putStrLn (show solution)

divByX :: (Integral a) => a -> a -> Bool
divByX x n = n `mod` x == 0

divBy3 = divByX 3
divBy5 = divByX 5

solution :: Integer
solution = sum [x |x <- [1..999], divBy3 x || divBy5 x]

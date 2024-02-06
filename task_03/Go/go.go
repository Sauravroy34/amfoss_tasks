package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	if num <= 1 {
		return false // 0 and 1 are not prime numbers
	}

	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false // num is divisible by i, so it's not a prime
		}
	}

	return true // num is prime
}

func main() {
	var n int
	fmt.Print("Enter a number (n): ")
	fmt.Scan(&n)

	fmt.Printf("Prime numbers up to %d:\n", n)

	for i := 2; i <= n; i++ {
		if isPrime(i) {
			fmt.Printf("%d ", i)
		}
	}

	fmt.Println()
}


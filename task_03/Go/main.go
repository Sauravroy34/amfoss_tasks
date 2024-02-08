package main

import "fmt"

func main() {
	var number int

	fmt.Println("enter a number")
	fmt.Scan(&number)

	if number <= 1 {
		fmt.Println("prime number not defined")

	} else {
		for j := 2; j <= number; j++ {
			if check(j) {
				fmt.Println("prime numer", j)
			}
		}
	}

}
func check(num int) bool{
	if num == 2 {
		return true
	}

	for i := 2; i < num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
 }

package main

import "fmt"

var memo = []int{-1}

func f(x int) int {
	if x == 0 || x == 1 {
		return 1
	} else {
		if memo[x] != -1 {
			return memo[x]
		} else {
			memo[x] = f(x-1) + f(x-2)
			return memo[x]
		}
	}
}
func main() {
	for i := 0; i < 1001; i++ {
		memo = append(memo, -1)
	}
	fmt.Println(f(4))
}

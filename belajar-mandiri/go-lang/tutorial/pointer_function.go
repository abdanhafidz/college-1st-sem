package main

import "fmt"

func plusinc(x *int) {
	*x += 1
}

func bernilai(x int) int {
	return x*5 + 2
}
func main() {
	x := 5
	plusinc(&x)
	y := 6
	plusinc(&y)
	fmt.Println("x:", x, "y:", y)
	var a int = bernilai(5)
	b := &a
	*b += 2
	fmt.Println("a:", a)

}

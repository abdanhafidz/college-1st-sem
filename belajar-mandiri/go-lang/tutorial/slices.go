package main

import (
	"fmt"
)

func main() {
	x := []int{1, 2, 3, 4, 5, 6, 10}
	var lgt int = len(x)
	var capt int = cap(x)
	fmt.Println(x[2:5])
	fmt.Println("panjang:", lgt)
	fmt.Println("apa itu cap?:", capt)
	x.append(7)
	fmt.Println("x index ke-2 adalah", x[2])

}

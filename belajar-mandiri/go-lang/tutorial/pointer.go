package main

import (
	"fmt"
)

func main() {
	var x int = 5
	var y int = x
	y += 1
	fmt.Println("Nilai y :", y, "Nilai x :", x, "Nilai x tidak berubah karena kita increase si y saja")
	var a int = 3
	var b *int = &a
	*b += 1
	fmt.Println("Nilai b :", *b, "Nilai a :", a, "Nilai a berubah karena sejatinya b adalah a yang dideclare dengan nama baru sehingga ketika b dioperasikan itu sama dengan mengoperasikan a")

	var blok = [3][3]int{{1, 2, 3}, {0, 0, 2}, {1, 2, 2}}
	var blok_1_2 int = *(&blok[1][2])
	fmt.Println("Blok 1,2 :", blok_1_2)

}

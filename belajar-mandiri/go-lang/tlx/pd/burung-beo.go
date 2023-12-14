package main

import (
	"fmt"
)

func main() {
	var S string
	for fmt.Scanln(&S) == true {
		fmt.Println(S)
	}
}

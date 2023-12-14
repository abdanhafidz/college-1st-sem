package main

import "fmt"

type user struct {
	id_user  int
	name     string
	email    string
	username string
	password string
}

func main() {
	var user1 = user{
		1,
		"Abdan",
		"abdan.hafidz@gmail.com",
		"mengCP",
		"12345",
	}
	who := *(&user1)
	who.id_user += 1
	fmt.Println(who)
}

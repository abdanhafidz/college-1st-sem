package main

import (
	"fmt"
)

// model
type user struct {
	id_user  int
	name     string
	email    string
	username string
	password string
}

func main() {
	var user1 user
	user1.id_user = 1
	user1.name = "Abdan"
	user1.email = "abdan.hafidz@gmail.com"
	user1.username = "mengCP"
	user1.password = "12345"

	var user2 = user{
		1,
		"Abdan",
		"abdan.hafidz@gmail.com",
		"mengCP",
		"12345",
	}
	fmt.Println("User 1 :", user1)
	fmt.Println("User 2 :", user2)
}

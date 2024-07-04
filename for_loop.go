package main

import "fmt"

func main() {

	i := 1
	var j = 1
	for i <= 3 {
		var j = 1
		j = i
		i = j
		fmt.Println(i)
		i = i + 1
	}
	fmt.Println("The value of j outside the for loop is ", j)
}

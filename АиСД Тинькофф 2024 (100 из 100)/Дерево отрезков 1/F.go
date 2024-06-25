package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	input  = bufio.NewReader(os.Stdin)
	output = bufio.NewWriter(os.Stdout)
)

func countGreater(mas []int, val int) int {
	c := 0
	for _, v := range mas {
		if v > val {
			c++
		}
	}
	return c
}

func countSmaller(mas []int, val int) int {
	c := 0
	for _, v := range mas {
		if v < val {
			c++
		}
	}
	return c
}

func result(mas []int) int {
	res := 0
	for i := 1; i < len(mas)-1; i++ {
		leftCount := countGreater(mas[:i], mas[i])
		rightCount := countSmaller(mas[i+1:], mas[i])
		res += leftCount * rightCount
	}
	return res
}

func main() {
	defer output.Flush()

	var n int
	fmt.Fscanln(input, &n)

	array := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(input, &array[i])
	}

	fmt.Fprintln(output, result(array))
}
package main

import "fmt"

func insertionSort(A []int) []int {
	l := len(A)
	for i := 1; i < l; i++ {
		cvalue := A[i]
		pos := i
		// fmt.Println(cvalue, pos, A[pos])
		for pos > 0 && A[pos-1] > cvalue {
			A[pos] = A[pos-1]
			// fmt.Println("vinod")
			pos = pos - 1
		}
		A[pos] = cvalue
	}

	return A
}

func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	fmt.Println("original:", A)
	insertionSort(A)
	fmt.Println(A)
}

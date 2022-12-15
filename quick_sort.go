package main

import "fmt"

func partition(A []int, left, right int) int {
	pivot := A[left]
	start := left
	end := right
	for start < end {
		for A[start] <= pivot {
			start += 1
		}
		for A[end] >= pivot {
			end -= 1
		}
		if start < end {
			A[start], A[end] = A[end], A[start]
		}
	}
	A[left], A[end] = A[end], A[left]

	// fmt.Println(end, A)
	return end
}

func quicksort(A []int, left, right int) {
	if left < right {
		// fmt.Println(left, right)
		loc := partition(A, left, right)
		quicksort(A, left, (loc - 1))
		quicksort(A, (loc + 1), right)
	}
}
func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	l := len(A) - 1
	fmt.Println(A)
	// quicksort(A, 0, l)
	quicksort(A, 0, l)
	fmt.Println(A)
}

package main

import "fmt"

func shellsort(A []int) []int {
	l := len(A)
	gap := (l / 2)

	for gap > 0 {
		// fmt.Println("* ******* *** **** ***")
		for i := 0; (i + gap) < l; i++ {
			if A[i] > A[i+gap] {
				A[i+gap], A[i] = A[i], A[i+gap]
				// fmt.Println(A)
				k := i - gap
				if k >= 0 && A[k] > A[i] {
					A[k], A[i] = A[i], A[k]
				}
			}
		}
		gap = gap / 2
	}
	return A
}

func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	fmt.Println("original", A)
	fmt.Println(shellsort(A))
}

package main

import "fmt"

func countsort(A []int) {
	l := len(A)
	m := A[0]
	for i := 1; i < l; i++ {
		if A[i] > m {
			m = A[i]
		}
	}
	carray := make([]int, m+1)
	for i := 0; i < l; i++ {
		carray[A[i]] += 1
	}
	fmt.Println(carray)
	i := 0
	j := 0
	for i <= m {
		if carray[i] > 0 {
			A[j] = i
			j += 1
			carray[i] -= 1
		} else {
			i += 1
		}

	}
}

func main() {
	A := []int{1, 2, 3, 4, 2, 3, 1, 3}
	fmt.Println(A)
	countsort(A)
	fmt.Println(A)
}

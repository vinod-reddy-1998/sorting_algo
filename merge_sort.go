package main

import "fmt"

func mergesort(A []int, left, right int) {
	if left < right {
		mid := (left + right) / 2
		mergesort(A, left, mid)
		mergesort(A, mid+1, right)
		merge(A, left, mid, right)
		//fmt.Println(mid)
	}
}
func merge(A []int, left int, mid int, right int) {
	i := left
	j := mid + 1
	k := left
	B := make([]int, right+1)
	for i <= mid && j <= right {
		if A[i] < A[j] {
			B[k] = A[i]
			//B = append(B, A[i])
			k += 1
			i += 1
		} else {
			// B = append(B, A[j])
			B[k] = A[j]
			k += 1
			j += 1
		}
	}
	for i <= mid {
		//B = append(B, A[i])
		B[k] = A[i]
		i += 1
		k += 1
	}
	for j <= right {
		// //B = append(B, A[j])
		B[k] = A[j]
		j += 1
		k += 1
	}
	for i := left; i < right+1; i++ {
		A[i] = B[i]
	}
}
func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	fmt.Println("original", A)
	mergesort(A, 0, len(A)-1)
	fmt.Println(A)

}

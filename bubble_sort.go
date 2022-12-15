package main

func bubbleSort(A []int) []int {
	l := len(A)
	for i := l - 1; i <= 0; i-- {
		for j := 0; j <= i; j++ {
			if A[i] > A[i+1] {
				temp := A[i]
				A[i] = A[i+1]
				A[i+1] = temp
			}
		}

	}
	return A
}

func bubbleSort2(A []int) []int {
	l := len(A)
	for i := 0; i <= l; i++ {
		for j := 0; j <= l-1-1; j++ {
			if A[j] > A[j+1] {
				A[j], A[j+1] = A[j+1], A[j]
			}
		}
	}
	return A
}

func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	print("original:", A)

	bubbleSort(A)
	print("sorted:", A)
}

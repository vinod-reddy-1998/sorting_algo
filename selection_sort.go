package main

func selectionSort(A []int) []int {
	l := len(A)
	for i := 0; i < l; i++ {
		min := i
		for j := i + 1; j <= l; j++ {
			if A[j] < A[min] {
				min = j
			}
		}
		tmp := A[i]
		A[i] = A[min]
		A[min] = tmp
	}
	return A
}

func main() {
	A := []int{3, 5, 7, 2, 1, 8}
	print("original:", A)

	selectionSort(A)
	print("sorted:", A)

}

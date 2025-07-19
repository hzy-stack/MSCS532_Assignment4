class HeapSorter:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def heapsort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)

        return self.arr

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Original array:", data)

    sorter = HeapSorter(data)
    sorted_array = sorter.heapsort()

    print("Sorted array:", sorted_array)
import random
import time


def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)


def test_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    distributions = {
        "Random": lambda n: random.sample(range(n * 10), n),
        "Sorted": lambda n: list(range(n)),
        "Reverse-Sorted": lambda n: list(range(n, 0, -1)),
    }

    algorithms = {
        "Heapsort": lambda arr: heapsort(arr.copy()),
        "Mergesort": lambda arr: mergesort(arr.copy()),
        "Quicksort": lambda arr: quicksort(arr.copy()),
    }

    for size in sizes:
        print(f"\nInput size: {size}")
        for dist_name, dist_fn in distributions.items():
            data = dist_fn(size)
            print(f"  Distribution: {dist_name}")
            for algo_name, algo_fn in algorithms.items():
                arr_copy = data.copy()
                start = time.time()
                algo_fn(arr_copy)
                end = time.time()
                print(f"    {algo_name}: {end - start:.6f} seconds")

if __name__ == "__main__":
    test_sorting_algorithms()

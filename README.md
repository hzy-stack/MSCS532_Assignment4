# MSCS532_Assignment4
MSCS532 Assignment4


### Run heapsort algorithm and sorting_comparisions
In MSCS532_Assignment4 folder, run command below
```shell
# Run randomized quick sort test
python3 heap_sorter.py
```

```shell
# Run sorting comparison.
python3 sorting_comparisons.py
```

Benchmark Result
```text
| Input Size | Distribution   | Heapsort | Mergesort | Quicksort |
| ---------- | -------------- | -------- | --------- | --------- |
| 1000       | Random         | 0.001616 | 0.001231  | 0.000953  |
|            | Sorted         | 0.001642 | 0.000781  | 0.000636  |
|            | Reverse-Sorted | 0.001557 | 0.000781  | 0.000546  |
| 5000       | Random         | 0.009168 | 0.005741  | 0.004217  |
|            | Sorted         | 0.008127 | 0.003543  | 0.002613  |
|            | Reverse-Sorted | 0.006778 | 0.003324  | 0.002642  |
| 10000      | Random         | 0.015221 | 0.009620  | 0.007676  |
|            | Sorted         | 0.015848 | 0.006408  | 0.004667  |
|            | Reverse-Sorted | 0.014052 | 0.006995  | 0.004688  |

```

### Run task schedule with min heap support
In MSCS532_Assignment4 folder, run command below
```shell
python3 task.py
```

### Summary of Finding
Heapsort offers consistent O(n log n) performance across all input types—random, sorted, or reverse-sorted—making it highly predictable. Unlike Quicksort and Mergesort, it does not benefit from input structure, showing minimal variation in runtime. This input-insensitivity and in-place behavior make Heapsort suitable for real-time or memory-constrained systems where worst-case guarantees matter more than raw speed.
However, in practice, Heapsort is slower than both Mergesort and Quicksort due to poor cache locality and frequent element swaps. While Quicksort excels in speed and Mergesort in stability, Heapsort trades these advantages for reliability and uniformity, which can be critical in certain system-level applications.


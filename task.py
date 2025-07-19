class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # Min-heap by priority

    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"


class TaskHeap:
    def __init__(self):
        self.heap = []
        self.task_index = {}  # Map task_id to index in heap

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        index = len(self.heap) - 1
        self.task_index[task.task_id] = index
        self._heapify_up(index)

    def extract_min(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        last = self.heap.pop()
        del self.task_index[root.task_id]
        if self.heap:
            self.heap[0] = last
            self.task_index[last.task_id] = 0
            self._heapify_down(0)
        return root

    def decrease_key(self, task_id, new_priority):
        if task_id not in self.task_index:
            return False
        index = self.task_index[task_id]
        if new_priority > self.heap[index].priority:
            return False  # Invalid decrease
        self.heap[index].priority = new_priority
        self._heapify_up(index)
        return True

    def increase_key(self, task_id, new_priority):
        if task_id not in self.task_index:
            return False
        index = self.task_index[task_id]
        if new_priority < self.heap[index].priority:
            return False  # Invalid increase
        self.heap[index].priority = new_priority
        self._heapify_down(index)
        return True

    def _heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def _swap(self, i, j):
        self.task_index[self.heap[i].task_id], self.task_index[self.heap[j].task_id] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    heap = TaskHeap()

    heap.insert(Task(1, 5, 0, 10))
    heap.insert(Task(2, 3, 1, 8))
    heap.insert(Task(3, 4, 2, 9))

    print("Extracted:", heap.extract_min())  # Task 2
    heap.decrease_key(1, 2)
    print("Extracted:", heap.extract_min())  # Task 1
    heap.increase_key(3, 10)
    print("Extracted:", heap.extract_min())  # Task 3

def siftDown(index, heap):
	heap_size = len(heap)
	while  2 * index + 1 < heap_size:
		left, right = 2 * index + 1, 2 * index + 2
		if right < heap_size:
			# two children
			child_min, id_min = min((heap[left], left), (heap[right], right), key=lambda z: z[0])
			if heap[index] < child_min:
				return heap
			heap[index], heap[id_min] = heap[id_min], heap[index]
			index = id_min
		else:
			#one child
			if heap[index] < heap[left]:
				return heap
			heap[index], heap[left] = heap[left], heap[index]
			index = left
	return heap



def siftUp(index, heap):
	while index > 0 and heap[(index - 1) // 2] > heap[index]:
		heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
		index = (index - 1) // 2
	return heap

def make_heap(heap):
	ans = []
	heap_size = len(heap)
	for i in range(heap_size // 2, -1, -1):
		heap = siftDown(i, heap)
	return heap


	
max_size, process_n = list(map(int, input().split()))
times = list(map(int, input().split()))
timeline = cur_size = 0
heap = [[0, i] for i in range(max_size)] 
answer = []
for elem in times:
	print(heap[0][1], heap[0][0])
	heap[0][0] += elem
	heap = siftDown(0, heap)

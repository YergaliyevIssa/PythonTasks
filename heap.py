def siftDown(index, heap, ans):
	heap_size = len(heap)
	while  2 * index + 1 < heap_size:
		left, right = 2 * index + 1, 2 * index + 2
		if right < heap_size:
			# two children
			child_min, id_min = min((heap[left], left), (heap[right], right), key=lambda z: z[0])
			if heap[index] < child_min:
				return heap, ans	
			ans.append((index, id_min))
			heap[index], heap[id_min] = heap[id_min], heap[index]
			index = id_min
		else:
			#one child
			if heap[index] < heap[left]:
				return heap, ans
			ans.append((index, left))
			heap[index], heap[left] = heap[left], heap[index]
			index = left
	return heap, ans



def siftUp(index, heap):
	while index > 0 and heap[(index - 1) // 2] > heap[index]:
		heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
		index = (index - 1) // 2
	return heap

def make_heap(heap):
	ans = []
	heap_size = len(heap)
	for i in range(heap_size // 2, -1, -1):
		heap, ans = siftDown(i, heap, ans)
	return heap, ans


	


n = int(input())
heap = list(map(int, input().split()))
heap, ans = make_heap(heap)
if len(ans):
	for i in ans:
		print(*i)
else:
	print(0)
#print(len(heap.exchange))
#for i in heap.exchange:
#	print(i)
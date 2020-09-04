
n = int(input())
t = list(map(int, input().split()))

def bin_search(a, key):
	l, r = 0, len(a)
	while r - l > 1:
		mid = (l + r) // 2
		if a[mid] <= key:
			l = mid
		else: 
			r = mid
	return l 

def find_depth(root, tree, leaf, inside_v):
	depth = 1
#	path = [leaf]
	while leaf != root:
		leaf = tree[leaf]
#		path.append(leaf)
		depth += 1
		if inside_v[leaf] > depth:
			break
		elif inside_v[leaf] < depth:
			inside_v[leaf] = depth

#	print(depth + 1, path)
	return depth

"""
def make_tree(tree, n):
	new_tree = [[] for i in range(n)]
#	print(new_tree[0])
	for child, parent in enumerate(tree):
		if parent != -1:
			new_tree[parent].append(child)
	print(new_tree)
	return new_tree
"""

root = t.index(-1)
#t = make_tree(t, n)
sorted_tree = t.copy()
sorted_tree.sort()
leaves = []
inside_v = [1] * n 
for i in range(n):
	index = bin_search(sorted_tree, i)
	if sorted_tree[index] != i:
		leaves.append(i)


#print(root, leaves)
depth = 1
for leaf in leaves:
	depth = max(depth, find_depth(root, t, leaf, inside_v))

print(depth)
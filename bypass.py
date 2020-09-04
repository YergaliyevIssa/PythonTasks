def InOrder(tree, i):
	if tree[i][1] != -1:
		InOrder(tree, tree[i][1])
	print(tree[i][0], end =' ')
	if tree[i][2] != -1:
		InOrder(tree, tree[i][2])


def PreOrder(tree, i):
	print(tree[i][0], end = ' ')
	if tree[i][1] != -1:
		PreOrder(tree, tree[i][1])
	if tree[i][2] != -1:
		PreOrder(tree, tree[i][2])
		

def PostOrder(tree, i):
	if tree[i][1] != -1:
		PostOrder(tree, tree[i][1])
	if tree[i][2] != -1:
		PostOrder(tree, tree[i][2])
	print(tree[i][0], end = ' ')



n = int(input())
tree = [list(map(int, input().split())) for i in range(n)]

InOrder(tree, 0)
print()
PreOrder(tree, 0)
print()
PostOrder(tree, 0)
print()


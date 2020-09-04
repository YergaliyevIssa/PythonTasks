import sys

sys.setrecursionlimit(20000)


def InOrder(tree, i, answer):
	if tree[i][1] != -1:
		answer = InOrder(tree, tree[i][1], answer)
	answer.append((tree[i][0], i))
	if tree[i][2] != -1:
		answer = InOrder(tree, tree[i][2], answer)
	return answer


def rfind(tree, v1, r):
	if v1 == -1:
		return False
	if tree[v1][0] == r:
		return True
	if r < tree[v1][0]:
		return rfind(tree, tree[v1][1], r)
	if r > tree[v1][0]:
		return rfind(tree, tree[v1][1], r)


	

n = int(input())

tree = [list(map(int, input().split())) for i in range(n)]
F = True

if n > 0:
	answer = InOrder(tree, 0, [])
	for i in range(n - 1):
		if answer[i][0] > answer[i + 1][0]:
			F = False
			break
		elif answer[i][0] == answer[i + 1][0]:
			if not rfind(tree, tree[answer[i][1]][2], answer[i][0]):
				F = False
				break
	#print(answer)


print('CORRECT' if F else 'INCORRECT')
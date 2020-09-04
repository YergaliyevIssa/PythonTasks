def get_id(elem, parent_list):
	while parent_list[elem] != elem:
		elem = parent_list[elem]
	return elem


n, e, d = list(map(int, input().split()))

parent_list = [i for i in range(n)]
rang = [0 for i in range(n)]
answer = True


def union(x, y, parent_list, rang):
	x_id = get_id(x, parent_list)
	y_id = get_id(y, parent_list)
	if rang[x_id] < rang[y_id]:
		parent_list[x_id] = y_id
	else:
		parent_list[y_id] = x_id
		if rang[x_id] == rang[y_id]:
			rang[x_id] += 1

	return parent_list, rang 




for i in range(e):
	p, q = list(map(int, input().split()))
	parent_list, rang = union(p - 1, q - 1, parent_list, rang)


for i in range(d):
	p, q = list(map(int, input().split()))
	if get_id(p - 1, parent_list) == get_id(q - 1, parent_list):
		answer = False
		break

print(int(answer))
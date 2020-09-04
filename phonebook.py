n = int(input())

table = [-1] * 10000000

for i in range(n):
	query = input().split()
	if query[0] =='add':
		table[int(query[1])] = query[2]
	elif query[0] == 'del':
		table[int(query[1])] = -1
	else:
		print('not found' if table[int(query[1])] == -1 else table[int(query[1])])
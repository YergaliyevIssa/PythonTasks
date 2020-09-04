def MakeSet(n):
	return [i for i in range(n)]


def FindRealTable(table, table_id):
	path_opt = []
	while table[table_id] != table_id:
		path_opt.append(table_id)
		table_id = table[table_id]
	for table_ind in path_opt:
		table[table_ind] = table_id
	return table_id

table_n, query_n = list(map(int, input().split()))
r_size = list(map(int, input().split()))
r_max, answer = max(r_size), [0] * query_n
table  = MakeSet(table_n)

for query in range(query_n):
	source, dest = list(map(int, input().split()))
	r_source = FindRealTable(table, source - 1)
	r_dest = FindRealTable(table, dest - 1)
	if r_dest != r_source:
		r_size[r_dest] += r_size[r_source]
		r_size[r_source] = 0
		table[r_source] = r_dest
	r_max = max(r_max, r_size[r_dest])
	answer[query] = r_max

for i in answer:
	print(i)
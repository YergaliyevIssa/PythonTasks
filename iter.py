import itertools

for j, i in enumerate(itertools.cycle([1, 2, 3])):
	if j > 10:
		break
	print(i)
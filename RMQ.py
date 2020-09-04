n = int(input())
a = list(map(int, input().split()))
m = int(input())


def preprocessing(a, n, m):
	b = [0] * n
	block_size = n // (m - 1)
	for block in range(block_size):
		offset = block * (m - 1)
		b[offset] = a[offset]
		for i in range(1, m - 1):
			b[offset + i] = max(b[offset + i - 1], a[offset + i])
		
	offset = (block + 1) * (m - 1)
	if n % (m - 1) != 0:
		b[offset] = a[offset]
	for i in range(1, n % (m - 1) ):
		b[offset + i] = max(b[offset + i - 1], a[offset + i])


	c = [0] * n
	for block in range(block_size):
		offset = block * (m - 1)
		c[offset + m - 2] = a[offset + m - 2]
		for i in range(m - 3, -1, -1):
			c[offset + i] = max(c[offset + i + 1], a[offset + i])
#идея использовать отрицательные индексы для простоты реализации
	#offset = (block + 1) * (m - 1)
	c[-1]=a[-1]
	for i in range(-2, -1 * (n % (m - 1)) - 1, -1):
		c[i] = max(c[i + 1], a[i])
	#print(b, c, sep='\n')
	return b, c

if (m > 1):
	b, c = preprocessing(a, n, m)
	ans = [0] * (n - m + 1)
	for l in range(n - m + 1):
		ans[l] = max(c[l], b[l + m - 1])
	print(*ans)
else:
	print(*a)


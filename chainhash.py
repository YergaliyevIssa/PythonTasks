def print_ans(asnwer):
	for i in answer:
		print(i)



def compute_x(x, p):
	X = [1] * 15
	X[0] = 1
	for i in range(1, 15):
		X[i] = (X[i - 1] * x) % p
	return X


class HashTable:
	def __init__(self, size, p=1000000007, x=263):
		self.table = [[] for i in range(size)]
		self.p = p
		self.size = size
		self.X = compute_x(x, p)

	def compute_hash(self, elem):
		hash_t = 0
		for i, char in enumerate(elem):
			hash_t = (hash_t + (self.X[i] * ord(char) % self.p)) % self.p

		#print(f'{elem} is element. {hash_t % self.size} is hash, {i}')
		return hash_t % self.size

	def add(self, elem):
		hash_t = self.compute_hash(elem)
		if elem not in self.table[hash_t]:
			self.table[hash_t].append(elem)


	def delete(self, elem):
		hash_t = self.compute_hash(elem)
		length  = len(self.table[hash_t])
		for i in range(length - 1, -1, -1):
			if self.table[hash_t][i] == elem:
				self.table[hash_t].pop(i)
				break

	def find(self, elem):
		hash_t = self.compute_hash(elem)
		return 'yes' if elem in self.table[hash_t] else 'no'

	def check(self, list_n):
		answer = self.table[list_n].copy()
		answer.reverse()
		return answer



m = int(input())
n = int(input())
hashtable = HashTable(m)
answer = []
for i in range(n):
	query = input().split()
	if query[0] == 'add':
		hashtable.add(query[1])
	elif query[0] == 'del':
		hashtable.delete(query[1])
	elif query[0] == 'find':
		z = hashtable.find(query[1])
		print(z)
		#answer.append(z)
	else:
		z = hashtable.check(int(query[1]))
		print(*z)
		#answer.append(z)



#print_ans(answer)
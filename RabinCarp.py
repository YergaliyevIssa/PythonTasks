def roll_hash(String, X, p, base):
	acc = 0
	for i, char in enumerate(String):
		acc = (acc + (X[i] * char) % p) % p 
	return acc	





def RabinKarp(pattern, source, X, p, base):
	m = len(pattern)
	answer = []
	pattern_hash = roll_hash(pattern, X, p, base)
	substr_hash = roll_hash( source[len(source) - m : len(source)], X, p, base)
	if pattern_hash == substr_hash:
		answer.append(len(source) - m)
	for i in range(len(source) - m - 1, -1, -1):
		substr_hash = ((substr_hash - (X[-1] * source[i + m]) % p + p) % p * base % p + source[i]) % p
		if pattern_hash == substr_hash:
			answer.append(i)
	answer.reverse()
	return answer





pattern = list(map(ord, input()))
source = list(map(ord, input()))

p ,base =1000000007, 263 
X = [1] * len(pattern) 
for i in range(1, len(pattern)):
	X[i] = (X[i - 1] * base) % p
	

print(*RabinKarp(pattern, source, X, p, base))
	

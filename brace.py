inp = input()


def check_seq(inp):
	stack = []
	ind = []
	for index, brace in enumerate(inp):
		if brace in ('[', '{', '('):
			stack.append(brace)
			ind.append(index + 1)
		elif brace in (']', '}', ')'):
			if len(stack) == 0:
				return index + 1
			if (brace == ')' and stack[-1] == '(') or (brace == '}' and stack[-1] == '{') or (brace == ']' and stack[-1] == '['):
				stack.pop()
				ind.pop()
			else:
				return index + 1
	return "Success" if len(stack) == 0 else ind[-1]



print(check_seq(inp))



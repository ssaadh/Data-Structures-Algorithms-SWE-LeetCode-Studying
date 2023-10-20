

def is_valid_parenthesis(s):
	stack = []
	for char in s:
		if char == "(":
			stack.append(char)
		elif char == ")":
			# Check if the stack is empty. If empty, then return false since 
			# we have more ")" than "("
			if len(stack) == 0:
				return False
			if stack.pop() != "(":
				return False
		# Otherwise we have a non-paren character which returns False.
		else:
			return False
	# If the stack is not empty, then we have more ")" to match and return False
	if len(stack) > 0:
		return False

	# Otherwise it's valid!
	return True


invalid_s = "(()"
print(is_valid_parenthesis(invalid_s))
valid_s = "(())()"
print(is_valid_parenthesis(valid_s))


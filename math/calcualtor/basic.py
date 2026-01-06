

# Leetcode Q224. Basic Calculator
# Given a string s representing a valid expression, implement a basic calculator to evaluate it,
# and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings
# as mathematical expressions, such as eval().


def calculate(s: str) -> int:

	signs = []
	result = [ 0 ]
	current = str()

	for char in s:
		match char:
			
			case "-":

				result[-1] += int(current or 0)
				current = "-"

			case "+":

				result[-1] += int(current or 0)
				current = str()

			case "(":

				result.append(0)
				signs.append(-1 if current else 1)
				current = str()

			case ")":

				result[-1] += int(current or 0)
				prev = result.pop() * signs.pop()
				result[-1] += prev
				current = str()

			case " ":	continue
			case _:		current += char

	return	result[-1] + int(current or 0)


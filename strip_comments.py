# easy try
def strip_comments_easy(strng: str, markers):
	lines = strng.split('\n')
	result = []

	for line in lines:
		for marker in markers:
			if marker in line:
				line = line.split(marker)[0]
		result.append(line.strip())
	print(result)
	return '\n'.join(result)

# hard try
# not found

result = strip_comments_easy("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

print(result)
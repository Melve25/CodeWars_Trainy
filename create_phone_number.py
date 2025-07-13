# easy try
def create_phone_number_easy(n):
	string = '('
	for i, val in enumerate(n):
		if i == 2:
			string = f"{string}{val}) "
			continue
		if i == 5:
			string = f"{string}{val}-"
			continue
		string = f'{string}{val}'
		

	return string

# hard try
def create_phone_number_hard(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number_easy([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
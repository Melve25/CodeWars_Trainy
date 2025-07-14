import string

# easy try
def is_pangram_easy(st):
	alf = [chr(i) for i in range(65, 91)]
	sentence = st.replace(' ','').upper()
	letters = []
	for letter in sentence:
		if ord(letter) in [i for i in range(65, 91)]:
			letters.append(letter)

	if sorted(set(letters)) == alf:
		return True
	return False

# hard try
def is_pangram_hard(st):
	alf = set(chr(i) for i in range(65, 91))
	letters = {c for c in st.upper() if "A" <= c <= "Z"}

	return letters >= alf

# super hard try
def is_pangram_super_hard(st):
	return set(string.ascii_uppercase) <= set(st.upper())

"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

print(is_pangram_super_hard("The quick brown fox jumps over the lazy dog"))

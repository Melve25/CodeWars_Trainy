import string
"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
"""

# easy try
def alphabet_position_easy(text):
    position = list(string.ascii_lowercase)
    output = ''
    for letter in text:
        if 'a' <= letter.lower() <= 'z':
            output += f'{str(position.index(letter.lower()) + 1)} '
            
    return output.strip()

# hard try
def alphabet_position_hard(text):
    return ' '.join(
        str(ord(c.lower()) - 96)
        for c in text
        if c.isalpha()
	)

print(alphabet_position_easy("The sunset sets at twelve o' clock."))
print(alphabet_position_hard("The sunset sets at twelve o' clock."))

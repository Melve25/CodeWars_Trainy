import string
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
# easy try
def pig_it(text: str):
    words = [
        word
        if word[0] not in string.ascii_letters else f'{word[1:-1]}{word[0]}ay{word[-1]}' 
        if word[-1] in string.punctuation else f'{word[1:]}{word[0]}ay'
        for word in text.split()
    ]

    return ' '.join(words)

print(pig_it('Hello, me is world !'))
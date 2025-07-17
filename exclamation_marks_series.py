"""
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
"""
# easy try
def balance_easy(left: str, right: str):
    left_sum = (lambda x, y: x*2 + y*3)(
        sum([l.count('!') for l in left]),
        sum([l.count('?') for l in left])
    )
    right_sum = (lambda x, y: x*2 + y*3)(
        sum([r.count('!') for r in right]),
        sum([r.count('?') for r in right])
    )
    if left_sum == right_sum:
        return 'Balance'
    
    if left_sum > right_sum:
        return 'Left'
    else:
        return 'Right'

# hard try
def balance_hard(left: str, right: str):
    left_sum = left.count('!')*2 + left.count('?')*3
    right_sum = right.count('!')*2 + right.count('?')*3
    
    if left_sum == right_sum:
        return 'Balance'
    
    if left_sum > right_sum:
        return 'Left'
    else:
        return 'Right'

print(balance_easy("!!", "??"))
print(balance_easy("!??", "?!!"))
print(balance_easy("!!???!????", "??!!?!!!!!!!"))

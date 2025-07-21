"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

# easy try
def move_zeros_easy(lst: list):
    new_list = [item for item in lst if item != 0]
    zeros = [0] * (len(lst) - len(new_list))
    return [*new_list, *zeros]




print(move_zeros_easy([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros_easy([0, 0, 1]))
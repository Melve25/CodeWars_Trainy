"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
"""

def circle(index: int, snail_map: list[list[int]]):
	# NOTE: RIGHT
	resp = snail_map[index : index+1][0][index : int(len(snail_map)-index)]

	# NOTE: DOWN
	for s in snail_map[index+1 : int(len(snail_map)-index)]:
		resp.append(s[len(snail_map)-1-index])

	# NOTE: LEFT
	for s in list(
		reversed(
			snail_map[int(len(snail_map)-(index+1))][index : -(index+1)]
		)
	):
		resp.append(s)

	# NOTE: UP
	for s in list(
		reversed(
			snail_map[index + 1: -index-1]
		)
	):
		resp.append(s[index])

	return resp

def snail_easy(snail_map: list[list[int]]):
	resp = []
	index = 0
	if len(snail_map) % 2 != 0:
		index = 1
	for i in range(int(len(snail_map) / 2) + index):
		resp += circle(i, snail_map=snail_map)

	return resp


def snail_hard(array):
    result = []
    while array:
        result += array.pop(0)
        
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        
        if array:
            result += array.pop()[::-1]
        
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
                
    return result




# print(snail_easy([
# 	[1,2],
# 	[8,9]
# ]))

# print(snail_easy([
# 	[1,2,3],
# 	[8,9,4],
# 	[7,6,5]
# ]))

# print(snail_hard([
# 	[1,2],
# 	[8,9]
# ]))

# print(snail_hard([
# 	[1,2,3],
# 	[8,9,4],
# 	[7,6,5]
# ]))

print(snail_hard([
	[1, 2, 3, 4],
	[12,13,14,5],
	[11,16,15,6],
    [10,9, 8, 7]
]))
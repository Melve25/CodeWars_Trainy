# easy try
def sumin_easy(n):
    nums = []
    for i in range(n):
        for j in range(n):
            nums.append(min(i + 1, j + 1))
    return sum(nums)
    
def sumax_easy(n):
    nums = []
    for i in range(n):
        for j in range(n):
            nums.append(max(i + 1, j + 1))
    return sum(nums)
    
def sumsum_easy(n):
    nums = []
    for i in range(n):
        for j in range(n):
            nums.append((i + 1) + (j + 1))
    return sum(nums)



# f: 1<= x <= n, 1<= y <=n --> f(x, y) = min(x, y)
# g: 1<= x <= n, 1<= y <=n --> g(x, y) = max(x, y)
# h: 1<= x <= n, 1<= y <=n --> h(x, y) = x + y

# hard try
def sumin_hard(n):
    total = 0
    count = 1
    for i in range(n):
        total += (n - i) * count
        count += 2
    return total

def sumax_hard(n):
    total = 0
    count = 1
    for i in range(n):
        total += (i + 1) * count
        count += 2
    return total

def sumsum_hard(n):
	return n * n * (n + 1)

# completed 11003 ms
print(sumin_easy(6))
print(sumax_easy(6))
print(sumsum_easy(6))

# completed 69 ms
print(sumin_hard(6))
print(sumax_hard(6))
print(sumsum_hard(6))
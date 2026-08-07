input_data = open("/home/advent-of-code-2022/Day04/advent_of_code_4.txt", "r")
input_data_lst = input_data.read().splitlines()
ans = 0
for line in input_data_lst:
	left, right = line.split(',')
	left_low, left_high = left.split('-')
	right_low, right_high = right.split('-')
	a, b = set(range(int(left_low), int(left_high) + 1)), set(range(int(right_low), int(right_high) + 1))
	result = a.intersection(b)
	if result:
		ans += 1
print(ans)
input_data.close()
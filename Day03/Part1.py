input_data = open("/home/advent-of-code-2022/Day03/advent_of_code_3.txt", "r")
input_data_lst = input_data.read().splitlines()
ans = 0
for line in input_data_lst:
	len_line = len(line)
	left, right = set(line[:len_line//2]), set(line[len_line//2:])
	results = left.intersection(right)
	for result in results:
		if 'a' <= result <= 'z':
			ans += ord(result) - ord('a') + 1
		else:
			ans += 26 + ord(result) - ord('A') + 1
print(ans)
input_data.close()
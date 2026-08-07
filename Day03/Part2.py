input_data = open("/home/advent-of-code-2022/Day03/advent_of_code_3.txt", "r")
input_data_lst = input_data.read().splitlines()
ans = 0
for index in range(0,len(input_data_lst),3):
	results = set(input_data_lst[index]) & set(input_data_lst[index + 1]) & set(input_data_lst[index + 2])
	for result in results:
		if 'a' <= result <= 'z':
			ans += ord(result) - ord('a') + 1
		else:
			ans += 26 + ord(result) - ord('A') + 1
print(ans)
input_data.close()
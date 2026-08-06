input_data = open("/home/advent-of-code-2022/Day01/advent_of_code_1.txt", "r")
input_data_lst = input_data.read().splitlines()
input_data_lst.append("")
max_num, curr_num = 0,0
for line in input_data_lst:
	if line == "":
		if curr_num > max_num:
			max_num = curr_num
		curr_num = 0
		continue
	curr_num += int(line)
print(max_num)
input_data.close()
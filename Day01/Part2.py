input_data = open("/home/advent-of-code-2022/Day01/advent_of_code_1.txt", "r")
input_data_lst = input_data.read().splitlines()
max_num, sec_num, third_num, curr_num = 0,0,0,0
input_data_lst.append("")
for line in input_data_lst:
	if line == "":
		if curr_num > max_num:
			third_num = sec_num
			sec_num = max_num
			max_num = curr_num
		elif curr_num > sec_num:
			third_num = sec_num
			sec_num = curr_num
		elif curr_num > third_num:
			third_num = curr_num
		curr_num = 0
		continue
	curr_num += int(line)
print(max_num + sec_num + third_num)
input_data.close()
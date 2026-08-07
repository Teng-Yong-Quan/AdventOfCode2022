input_data = open("/home/advent-of-code-2022/Day02/advent_of_code_2.txt", "r")
input_data_lst = input_data.read().splitlines()
score_dict = {'A' : {'X' : 3 + 1, 'Y': 6 + 2, 'Z': 0 + 3},
			'B' : {'X' : 0 + 1, 'Y': 3 + 2, 'Z': 6 + 3}, 
			'C' : {'X' : 6 + 1, 'Y': 0 + 2, 'Z': 3 + 3}}
score = 0
for line in input_data_lst:
	opp, me = line.split(' ')
	score += score_dict[opp][me]
print(score)
input_data.close()
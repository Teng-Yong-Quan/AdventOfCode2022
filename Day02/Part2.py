input_data = open("/home/advent-of-code-2022/Day02/advent_of_code_2.txt", "r")
input_data_lst = input_data.read().splitlines()
score_dict = {'A' : {'X' : 3 + 0, 'Y': 1 + 3, 'Z': 2 + 6},
			'B' : {'X' : 1 + 0 , 'Y': 2 + 3, 'Z': 3 + 6}, 
			'C' : {'X' : 2 + 0, 'Y': 3 + 3, 'Z': 1 + 6}}
score = 0
for line in input_data_lst:
	opp, me = line.split(' ')
	score += score_dict[opp][me]
print(score)
input_data.close()
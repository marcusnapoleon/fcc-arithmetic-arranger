def arithmetic_arranger(problems, solve_problem=False):

	###  ==>  TEST REQUIREMENT: Determines if there are more than 5 problems,
	###       if not creates/prepares empty variables.
	
	if len(problems) > 5:
		return "Error: Too many problems."
	else:
		top_row = ''
		mid_row = ''
        
		dsh_row = ''
		ans_row = ''

		longest_digit = 0
		problem_count = 0

		# ==> Iterates through each of the problem, splits each problem in into sections of a question
		for problem in problems:
			#print('problem count ==> ', problem_count)
            #print('problem ==> ', problem)
			problem_split = problem.split(' ')
            #print('problem split ==> ', problem_split)
            

			# ==> Assigns a meaningful name to the extracted section from the problem - 'top_number', 'operator', 'bottom_number'
			top_number = problem_split[0]
			operator = problem_split[1]
			bottom_number = problem_split[2]


			# ==> Creates a list of valid operator signs used in the problems, will be used to determine if an invalid operator has been used.
			operator_sign = ['+', '-']
            #print('top number ==> ', top_number)
            #print('operator ==> ', operator)
            #print('bottom number ==> ', bottom_number)
            #print('operator sign ==> ', operator_sign)


			# ==> Compares and determines which of the problem numbers have the longer digits - top or bottom number, then assigns to a variable 'longest_digit'
			top_num_len = len(top_number)
			btm_num_len = len(bottom_number)
			if top_num_len > btm_num_len:
				longest_digit = top_num_len
                #print('top num long ==> ', longest_digit)
			elif top_num_len < btm_num_len:
				longest_digit = btm_num_len
                #print('bottom num long ==> ', longest_digit)
			elif top_num_len == btm_num_len:
				longest_digit = top_num_len
                #print('top/btm same length ==> ', longest_digit)
            #print('longest digit ==> ', longest_digit)


			###  ==>  TEST REQUIREMENT: Determine the lengths of the top and bottom numbers, 
			###       will show an error if either number have more than 4 digits.
			if top_num_len > 4:
				return "Error: Numbers cannot be more than four digits."
			if btm_num_len > 4:
				return "Error: Numbers cannot be more than four digits."


			###  ==>  TEST REQUIREMENT: Using the 'operator_sign' list to compare/determine 
			###       if the problem operator is in the list, will show an error if sign is not.
			if operator not in operator_sign:
				return "Error: Operator must be '+' or '-'."


            ###  ==>  TEST REQUIREMENT: Using a built-in method '.isdigit()' to determine if 
			###       the top and bottom numbers are 'digits', will show an error if number is not a digit.
			if not top_number.isdigit():
				return "Error: Numbers must only contain digits."
			if not bottom_number.isdigit():
				return "Error: Numbers must only contain digits."


			# ==> Determines the type of operator and performs the calculations - Addtion if '+' / Subtraction if '-'.
			if operator == '+':
				answer = int(top_number) + int(bottom_number)
                #print('add answer ==> ', answer)
			if operator == '-':
				answer = int(top_number) - int(bottom_number)
                #print('sub answer ==> ', answer)
            #print('answer ==> ', answer)


			# ==> Creates a variable that represents 'longest_digit' length plus '2', for the single space between the operator and the longest of the two numbers.
			spanner = longest_digit + 2
            #print('span ==> ', spanner)
            

			# ==> Assigns the formatted values from the extracted section after the '.split()' to the variables representing question section/structure/answer.
			top_row += top_number.rjust(spanner)
			mid_row += operator + bottom_number.rjust(spanner - 1) 
			dsh_row += '-' * spanner
			ans_row += str(answer).rjust(spanner)       


			# ==> Creates a variable containing 4 spaces.
			blank_space = '    '
            #print('len pr spc ==> ', len(blank_space))


			# ==> Adds to the problem counter and determines if there are still questions in the problems, 
			#     adds 'blank_space' to the end of each question section/structure/answer - four spaces between each problem.
			problem_count += 1
			if problem_count < len(problems):
				top_row += blank_space
				mid_row += blank_space
				dsh_row += blank_space
				ans_row += blank_space

				# ==> Cleans/Strips each question section/structure/answer row of unwanted characters
				top_row.rstrip()
				mid_row.rstrip()
				dsh_row.rstrip()
				ans_row.rstrip()


		# ==> Determines if the function was invoked/called with the second argument 'solve_problem' has been set to 'True', if so
		#     calculation results/answer performed will be displayed on output/return, if not, only the question will be shown.
		if solve_problem:
			arranged_problems = top_row + '\n' + mid_row + '\n' +  dsh_row + '\n' + ans_row
		else:
			arranged_problems = top_row + '\n' + mid_row + '\n' + dsh_row
		return arranged_problems



print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

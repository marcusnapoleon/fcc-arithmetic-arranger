def arithmetic_arranger(problems, solve_problem=False):
    ##print('problems ==> ', problems)
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        top_row = ''
        mid_row = ''
        
        dsh_row = ''
        ans_row = ''

        longest_digit = 0
        
        problem_count = 0


        for problem in problems:
            #print('problem count ==> ', problem_count)
            #print('problem ==> ', problem)
            problem_split = problem.split(' ')
            #print('problem split ==> ', problem_split)
            


            top_number = problem_split[0]
            operator = problem_split[1]
            bottom_number = problem_split[2]
            operator_sign = ['+', '-']
            #print('top number ==> ', top_number)
            #print('operator ==> ', operator)
            #print('bottom number ==> ', bottom_number)
            #print('operator sign ==> ', operator_sign)



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



            if top_num_len > 4:
                return "Error: Numbers cannot be more than four digits."
            if btm_num_len > 4:
                return "Error: Numbers cannot be more than four digits."



            if operator not in operator_sign:
                return "Error: Operator must be '+' or '-'."


            
            if not top_number.isdigit():
                return "Error: Numbers must only contain digits."
            if not bottom_number.isdigit():
                return "Error: Numbers must only contain digits."



            if operator == '+':
                answer = int(top_number) + int(bottom_number)
                #print('add answer ==> ', answer)
            if operator == '-':
                answer = int(top_number) - int(bottom_number)
                #print('sub answer ==> ', answer)
            #print('answer ==> ', answer)



            spanner = longest_digit + 2
            #print('span ==> ', spanner)
            blank_space = '    '
            #print('len pr spc ==> ', len(blank_space))



            top_row += top_number.rjust(spanner)
            mid_row += operator + bottom_number.rjust(spanner - 1) 
            dsh_row += '-' * spanner
            ans_row += str(answer).rjust(spanner)       



            problem_count += 1
            if problem_count < len(problems):
                top_row += blank_space
                mid_row += blank_space
                dsh_row += blank_space
                ans_row += blank_space


                top_row.rstrip()
                mid_row.rstrip()
                dsh_row.rstrip()
                ans_row.rstrip()


        if solve_problem:
            arranged_problems = top_row + '\n' + mid_row + '\n' +  dsh_row + '\n' + ans_row
        else:
            arranged_problems = top_row + '\n' + mid_row + '\n' + dsh_row
        return arranged_problems








print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

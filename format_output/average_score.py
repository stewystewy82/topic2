first_name = input('Enter first name:')
last_name = input('Enter last name:')

x = (last_name + ', ' + first_name)

years_alive = input('Enter your age:')

num_of_scores = 3

score_1 = (int(input('Write down score 1:')))
score_2 = (int(input('Write down score 2:')))
score_3 = (int(input('Write down score 3:')))
total = (score_1 + score_2 + score_3)

average = str(total / 3)

print(x + ' ' + 'age:' + " " + years_alive + " " + "average grade: " + average)

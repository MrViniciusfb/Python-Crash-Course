#21/07/2021

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number < 2 and number > 0:
		print('\n' + str(number) + 'st')
	elif number < 3:
		print('\n' + str(number) + 'nd')
	elif number < 4:
		print('\n' + str(number) + 'rd')
	else:
		print('\n' + str(number) + 'th')

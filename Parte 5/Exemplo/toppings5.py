#19/07/2021
#Caso a pizzaria tivesse uma seleção estável de ingredientes
	#poderia se usar uma tupla
avaible_toppings = ['mushrooms','olives','green peppers',
					'pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in avaible_toppings:
		print('Adding ' + requested_topping+ '.')
	else:
		print('Sorry,we dont have ' + requested_topping + '.')

print('\nFinished making your pizza!')

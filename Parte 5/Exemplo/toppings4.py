#19/07/2021

requested_toppings = []

#Importante!Quando o nome de uma lista é usado em uma instrução if,Python
	#devolve True se a lista contiver pelo menos um item, uma lista vazia
	#é avaliada como False
if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding ' + requested_topping +'.')
	print('\nFinished making you pizza!')
	
else:
	print("Are you sure you want a plain pizza?")

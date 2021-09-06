#14/07/2021

my_pizzas = ['calabresa','portuguesa','rúcula']

friend_pizzas = my_pizzas[:]

my_pizzas.append('peperonni')
friend_pizzas.append('chocolate')

print('My favorite pizzas are: ')
for pizza in my_pizzas:
	print('I love ' + str(pizza.title()))

print('I really love pizza!')

print("\nWhile mine friend's are:")
for pizza in friend_pizzas:
	print('He loves ' + str(pizza.title()))

print('You can see we love pizzas, but different ones')

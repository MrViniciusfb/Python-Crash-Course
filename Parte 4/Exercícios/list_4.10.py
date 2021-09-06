#14/07/2021

cars = ['lamborghini','fiat','audi','ferrari','porsche']

print('Os três primeiros itens da lista são: ')
for car in cars[:3]:
	print('\t' + str(car.title()))

print('\nOs três itens do meio da lista são: ')
for car in cars[1:4]:
	print('\t' + str(car.title()))

print('\nOs três últimos itens da lista são:')
for car in cars[-3:]:
	print('\t' + str(car.title()))

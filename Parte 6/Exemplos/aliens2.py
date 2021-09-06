#25/07/2021
#Aplicação de informação aninhadas

alien_0 = {'color' : 'green', 'points': 5}
alien_1 = {'color' : 'yellow', 'points': 10}
alien_2 = {'color' : 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#Código mais realista para um jogo
#Cria uma lista vazia para armazenar alienígenas
aliens = []

#Cria 30 alienígenas verdes
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

#Mostra os 5 primeiros alienígenas
for alien in aliens[:5]:	#Fatia dos 5 primeiros itens
	print(alien)
print("...")

#MOstra quantos alienígenas foram criados
#print("Total number of aliens is " + str(len(aliens)))

#Mudando a cor do alien ao decorrer do tempo

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['collor'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'
		
print('\n')

#MOstra os 5 primeiros alienígenas
for alien in aliens[:5]:
	print(alien)

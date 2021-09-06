#13/07/2021

#Fatiando listas
	#Já fora aprendido a como acessar elementos específicos e com todo de uma vez
	#Agora será a hora de aprender como fatiar uma lista e trabalhar com apenas um pedaço dela
		#Funciona parecido como a função range()
			#Basta dar ao python o começo e o fim na posição na lista, mas ele imitirá o último, portanto some 1 caso queira
			
players = ['charles','martina','michael','florence','eli']
#pritnando do primeiro ao segundo elemento da lista
print(players[0:3])
#caso se omita o primeiro número o python, automaticamente, começara do primeiro elemento
	#Assim como se não colocar o último, ele irá até o final. Isso independe do tamanho da lista
		#E caso não se coloque nem o inicial, nem o final, ele mostrará toda a lista [:] . Isso será muito útil logo adiante em foods.py
print(players[:3])
print(players[2:])

#Também há a possibilidade de usar um índice negativo
print(players[-2:])
	#Isso diz ao pthon para começar dos antepenuntimo elemnto e ir até o final

#Vamos agora percorrer uma fatia com um laço

print('Here are the last three players on my team: ')
for player in players[-3:]:
	print('\t'+str(player.title()))


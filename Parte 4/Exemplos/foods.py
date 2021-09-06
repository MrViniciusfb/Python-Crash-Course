#13/07/2021

#Muitas vezes haverá a necessidade de criar uma lista com elementos de uma já existente
	#Far-se-á isso com a fatiação, SEMPRE, com fatias.
		#Definir uma lista igual a outra acarretará problemas, o python entenderá que elas são, na verdade, a mesma lista
	#Bata, portanto, utilizar [:] caso se queira copiar toda a lista, ou apenas um pedaço com o já conhecido modo de fatiar
	
my_foods = ['pizza','hotdog','tropeiro']
friends_foods = my_foods[:]
	#Meu amigo gosta de tudo o que gosto

#Para provar que o python não está tratando elas como se fossem apenas uma basta adicionar elementos distintos para cada uma

my_foods.append('sorvete')
friends_foods.append('bis')
friends_foods.insert(2,'chocolate')

print('My favorite foods are: ')
print('\t' + str(my_foods))

#Cuidado (errei aqui) usar "" quando precisar utilizar '
print("\nMy friend's favorite foods are:")
print('\t' + str(friends_foods))

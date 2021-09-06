#13/07/2021

#Tuplas são parecidas com listas, porém tem a caracteristica de serem imutáveis e usarem () em vez de [], nas listas

dimensions = (200,50)

#Para buscar um elemento da tupla basta afzer como em uma lista
print(dimensions[0])
print(dimensions[1])

#Para a nossa sorte,caso haja a tentativa de mudar o valor de uma tupla,por exemplo:
	#dimensions[0] = 250
		#Isso gerará um erro de tipo:
			# TypeError: 'tuple' object does not support item assignment

#Assim como em uma lista é possível percorrer os elementos de uma tupla com um laço
print('\nOriginal dimensions:')
for dimension in dimensions:
	print('\t'+ str(dimension))

#Caso se queria mudar uma tuplar, há a possibilidade de sobreescrevê-la, iso não acarretará em erros

dimensions = (400,100)
print('\nModified dimensions: ')

for dimension in dimensions:
    print('\t'+ str(dimension))
	

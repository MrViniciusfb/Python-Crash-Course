#09/07/2021

print('Lista sem alteração de ordem')
cars = ['bmw','audi','toyota','subaru']
print('\t' + str(cars))

#A função sorted() altera a ordem da lista de forma não permanente colocando-a em ordme alfabética
print('\nLista original:')
print('\t' + str(cars))

print('\nLista em ordeme alfabética temporária: ')
print('\t' + str(sorted(cars, reverse = False))) #Caso se queira colocar invetido,basta trocar por True

print('\nLista original novamente:')
print('\t' + str(cars))

#Método sort() altera a ordem da lista de forma permanente colocando-a em ordme alfabética

print('\nLista em ordem alfabética permanente:')
cars.sort()
print('\t'+ str(cars))

#Pode-se alterar  a ordem permanentemente colocando na ordem inversa do alfabeto
#sort(reverse=True)

print('\nLista em ordem inversa permanente: ')
cars.sort(reverse=True)
print('\t' + str(cars))
cars.sort(reverse=True)

#Para inverter a ordem de uma lista basta usar o método reverse() e para desenverter basta reaplicar o método
print('\nLista original: ')
print('\t' + str(cars))
print('\nLista invertida permanentemente: ')
cars.reverse()
print('\t' + str(cars))
print('\nLista novamente original: ')
cars.reverse()
print('\t' + str(cars))

#Para descobrir o tamanho de uma lista basta aplicar a funão len()
print('\nTodas as listas apresentadas possuem tamanho ' + str(len(cars)))

#10/07/2021

lugares_visitar = ['tailandia','nova iorque','tokyo','cingapura','alabama']
print('\nLista original:')
print('\t' + str(lugares_visitar))

print('\nLista em ordem alfabética não permanente:')
print('\t' + str(sorted(lugares_visitar, reverse = False)))
print('\nPercebe-se que a lista não foi alterada definitivamente: ')
print('\t' + str(lugares_visitar))

lugares_visitar.reverse()
print('\nLista na ordem contrária com o método reverse:')
print('\t' + str(lugares_visitar))
lugares_visitar.reverse()
print('\nLista na ordem original com o método reverse:')
print('\t' + str(lugares_visitar))

lugares_visitar.sort()
print('\nLista na ordem alfabética permanente: ')
print('\t'+ str(lugares_visitar))
lugares_visitar.sort(reverse = True)
print('\nLista na ordem alfabética inversa permanente: ')
print('\t' + str(lugares_visitar))



#09/07/2021
lista_convidados = ['john lennon','Elton John','michiu kaku']

print('1ª Lista de convites enviadas: ')
print('\tBom dia, Sr.' + str(lista_convidados[0].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[1].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[2].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\nInfelizmente o Sr.' + str(lista_convidados[0].title()) + ' não poderá comparecer\n')

lista_convidados[0] = 'Tim Maia'
print('2ª Lista de convites enviados:')
print('\tBom dia, Sr.' + str(lista_convidados[0].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[1].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[2].title()) + '! Aguardo-o para a festa no dia 09/07/2021')

print('\nCaros convidados, consegui uma reserva em uma mesa maior, portanto teremos mais convidados')
lista_convidados.insert(0, 'Mick Jagger')
lista_convidados.insert(2,'Albert Einsten')
lista_convidados.append('Igor 3K')

print('\n3ª Lista de convites enviados:')
print('\tBom dia, Sr.' + str(lista_convidados[0].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[1].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[2].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[3].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[4].title()) + '! Aguardo-o para a festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[5].title()) + '! Aguardo-o para a festa no dia 09/07/2021')

print('Caros amigos, infelizmente a mesa não chegará a tempo...Portanto, segue a lista dos atuais convidados')


print('\tBom dia, Sr.' + str(lista_convidados[5].title()) + '! Infelizmente terei que desconvidá-lo da festa no dia 09/07/2021')
popped_lista_convidados = lista_convidados.pop()

print('\tBom dia, Sr.' + str(lista_convidados[4].title()) + '! Infelizmente terei que desconvidá-lo da festa no dia 09/07/2021')
popped_lista_convidados = lista_convidados.pop()


print('\tBom dia, Sr.' + str(lista_convidados[3].title()) + '! Infelizmente terei que desconvidá-lo da festa no dia 09/07/2021')
del lista_convidados[3]

print('\tBom dia, Sr.' + str(lista_convidados[2].title()) + '! Infelizmente terei que desconvidá-lo da festa no dia 09/07/2021')
del lista_convidados[2]

print('\tBom dia, Sr.' + str(lista_convidados[0].title()) + '! Ainda o aguardo para festa no dia 09/07/2021')
print('\tBom dia, Sr.' + str(lista_convidados[1].title()) + '! Ainda o aguardo para festa no dia 09/07/2021')

print('Lista final de convidados: ')
print(lista_convidados)

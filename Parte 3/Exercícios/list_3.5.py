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


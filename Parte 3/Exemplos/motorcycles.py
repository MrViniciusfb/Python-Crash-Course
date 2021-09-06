#07/07/2021

print('Lista 1:')
motorcycles = ['honda','yamaha','suzuki']
print('\t' + str(motorcycles))

#Para modificar um elemento de uma lista basta fornecer a posição do elemento e o novo valor
print('\nLista com o primeiro valor modificado:')
motorcycles[0] = 'ducati'
print('\t'+ str(motorcycles))

#O método append() possibilita adicionar um elemento em uma lista ao final desta
print('\nLista com valor concatenado: ')
motorcycles.append('honda')
print('\t'+ str(motorcycles))

#Isso possibilitá-nos criar listas dinâmicas que começam vazias e são preenchidas
motos = []
print('\nLista 2: ')
motos.append('suzuki')
motos.append('lambreta')
motos.append('honda')

#Caso se tente misturar listas e string deve-se usar a função str()
print('\t' + str(motos))

#Também é possível inserir elementos em qualquer posição da lista com o método insert(posicao , 'valor')
print('\nLista com valor inserido na primeira posição: ')
motorcycles.insert(0, 'ninja')
print('\t'+ str(motorcycles))

#Há a possibilidade de remover elementos de uma lista
#A instrução del pode ser utilizada caso se conheça a posição de um item
print('\nLista com o primeiro elemento removido:')
del motorcycles[0]
print('\t' + str(motorcycles))

#ÀS vezes você vai querer usar o valor de um item depois de removê-lo de uma lista, para isso usa-se o método pop()
print('Lista mostrando a aplicação do método pop(): ')
print('\t'+ str(motorcycles))
popped_motorcycles = motorcycles.pop()
print('\t'+ str(motorcycles))
print('Obtendo o valor já excluido da lista:')
print('\t'+ str(popped_motorcycles.title())+ '.')

#O método pop() também pode ser utilizado para remover um item de qualquer posição
print('\nLista removendo o primeiro elemento com o método pop(): ')
first_owned = motorcycles.pop(0)
print('\tThe last motorcycle I owned was a '+ str(first_owned.title())+ '.')

#Caso haja dúvida em qual usar del ou pop(),lembre-se, caso você não queira usar os dados do elemento a ser retidado use del,caso contrário use pop()
#Já se você não conhce a posição e somente o valor do elemento, basta usar o método remove()
print('\nLista com valor removido quando não se conhece a posição do elemento a ser removido: ')
print('\t' + str(motorcycles))
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print('\t' + str(motorcycles))
print('\nA '+ too_expensive.title() + ' is too expensive for me.')

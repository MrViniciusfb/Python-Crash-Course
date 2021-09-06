#07/07/2021
#Listas são indicadas por [] e são uma coleção de itens em uma ordem particular
#Lembrar sempre que o primeiro elemento da lista é o elemento zero
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#Para indicar um elemento da lista basta colocar o nomeda lista e [posicao do elemento]
#E também é possível melhorar a saída adicionando os métodos de string já estudados.
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[2].lower())

#Caso queira acessar o último item da lista em python basta usar [-1],também é possível ultilizar [-2],[-3] e assim por diante caso se queira os itens a partir do final
print(bicycles[-1].title())

#É possível usar valores individuais de uma lista exatamente como faria com qualquer variável
message = "\nMy first bicycle was a " + bicycles[0].title() + "."
print(message)

#Os principais erros cometidos na lista são IndexError: list index out of range, é causado quando se procura um índice não existente na lista

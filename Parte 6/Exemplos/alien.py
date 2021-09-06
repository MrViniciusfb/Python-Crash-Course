#23/07/2021
#Os dicionários são definidos com par chaves ex tipo : valor ,
alien_0 = {'color': 'green', 'points': 5}

#Para printar um valor do par chave basta colocar o dicionario e em seguida
	#[par_chave]
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#Adicionando par chave ao dicionário
	#Posição do alien
		#Posição x y na tela a partir do canto inferior esquerdo
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Criando um dicionário vazio

alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

#Modificando os valores em um dicionário

print( "\nThis alien is " + str(alien_0['color']))

#Tentar mudar mais de um par chave não é possível
	#alien_0['color','points'] = 'yellow', 15
alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

#Removendo pares chaves-valor
	#Basta usar del dando o nome do diconário e o par chave
	#Notar, é removido de forma permanente
del alien_0['points']
print(alien_0)

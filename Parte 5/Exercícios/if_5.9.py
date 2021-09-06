#21/07/2021

users = []

#Lembre-se, o python retorna false se a lista estiver vazia
if users:
	for user in users:
		if user == 'admin':
			print('Olá, ' + str(user) +
					'! Gostaria de ver o novo relatório de status?')
		else:
			print('Olá ' + str(user.title()) +
					', obrigado por fazer o login novamente')
else:
	print('Precisamos de novos usuários')			

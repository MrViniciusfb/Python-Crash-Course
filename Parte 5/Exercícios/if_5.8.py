#21/07/2021

users = ['admin','ana','bessa','dalecko','lucao']


for user in users:
	if user == 'admin':
		print('Olá, ' + str(user) +
				'! Gostaria de ver o novo relatório de status?')
	else:
		print('Olá ' + str(user.title()) +
				', obrigado por fazer o login novamente')
			
			

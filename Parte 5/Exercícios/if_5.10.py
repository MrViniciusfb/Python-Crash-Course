#21/07/2021

current_users = ['ana','dalecko','bessa','lucas','romero','loli']

new_users = ['loli','reginaldo','daLEcko','sandra']

for new_user in new_users:
	if new_user.lower() in current_users:
		print('Nome já escolhido. Tente outro.')
	else:
		print('Nome disponível')

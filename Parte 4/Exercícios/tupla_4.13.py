#14/07/2021

dishes = ('batata','tropeiro','macarrão','peixes','churrasco')

print('\nThere are our dishes: ')
for dishe in dishes:
	print('\t' + str(dishe.title()))

#dishes[0] = 'ovo' vai dar erro

dishes = ('ovo','tropeiro','macarrão','tilapia','churrasco')

print('\nThere are our new list of dishes: ')
for dishe in dishes:
	print('\t' + str(dishe.title()))

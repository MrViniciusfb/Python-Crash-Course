#25/07/2021

user_0 = {
		'username' : 'efermi',
		'first' : 'erico',
		'last' : 'fermi',
}

#Para percorrer um dicionário é necessáro ciar nomes para duas variáveis que 
	#armazenarão a chave e o valor

for key,value in user_0.items(): 	#Método items() devolve uma lista de pares
	print("\nKey: " + key)			#chave-valor
	print("Value: " + value)

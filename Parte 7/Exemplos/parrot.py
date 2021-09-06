#31/07/2021

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. "

message = ""
#Código para o usuário decidir quando parar
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit': #Usa-se para não retornar quit no print
		print(message)
		message = ""
		
#Para caso existam muitas condições para o código continuar rodando deve-se
	#usar uma flag(Valor booleano), ela é uma bandeira para sinalizar o
	#funcionamento ou não do código
	
active = True
while active:
	message = input(prompt)
	
	#Pode-se colocar vários elif para parar o código se necessário
	if message == 'quit':
		active = False
	else:
		print(message)
	
#Há também a possibilidade de redirecionar o fluxo do seu programa ao usar
	#a instrução break. Ele para tudo sem executar o código restante

#Há também a possibildiade de usar a instrução continue que retorna ao início
	#com base no resultado de um teste condicional

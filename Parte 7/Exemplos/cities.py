#31/07/2021

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

#While true executa infinitamente o loop e para se encontrar a instrução break
while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
	
#O uso do break pode ser feito em qualquer laço de python até mesmo quando
	#percorrer dicionarios, listas e tuplas para parar de percorrê-los

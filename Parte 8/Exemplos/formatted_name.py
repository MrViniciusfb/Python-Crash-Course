#Sem nome do meio
def get_formatted_name(first_name, last_name):
	"""Devolve um nome completo formatado de modo elegante"""
	full_name = first_name + ' ' + last_name #Soma de strings as agrupa
	return full_name.title()

#Quando se chama uma função que devolve um valor, precisa-se fornecer uma 
	#variável em que o valor de retorno possa ser armazenado	
musician = get_formatted_name('jimi', 'handrix')
print(musician)

#Com nome do meio
	#A função só funciona caso se de todos os valores
def get_formatted_name2(first_name, middle_name, last_name):
	"""Devolve um nome completo formatado de modo elegante"""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()
	
musician = get_formatted_name2('john', 'lee', 'hooker')
print(musician)
	
#Com o nome do meio
	#A função funciona independente se há ou não nome do meio
def get_formatted_name3(first_name, last_name, middle_name = ''):
	"""Devolve um nome completo formatado de modo elegante""",
	if middle_name:	#Se n~middle_name não é vazia execute
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'handrix')
print(musician)

musician = get_formatted_name2('john', 'hooker', 'lee') #Argumentos posicionais
print(musician)

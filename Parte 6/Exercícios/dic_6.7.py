#26/07/2021

pessoa0 = {'first_name' : 'André',
		'last_name' : 'Daleck',
		'age' : 18,
		'city' : 'São José do Rio Preto'
}
pessoa1 = {'first_name' : 'Samuel',
		'last_name' : 'Laureano',
		'age' : 19,
		'city' : 'Londrina'
}
pessoa2 = {'first_name' : 'Vinícius',
		'last_name' : 'Bessa',
		'age' : 19,
		'city' : 'Cingapura'
}

people = [pessoa0, pessoa1, pessoa2]

for pessoa in people:
	print('His name is ' + str(pessoa['first_name']) + 
			' ' + str(pessoa['last_name']) + 
			' and his age is ' + str(pessoa['age']) +
			". Now he's living in " + str(pessoa['city'])) #Tomar cuicado com falta de parenteses EOF error

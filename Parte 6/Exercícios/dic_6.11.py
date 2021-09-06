#26/07/2021

cities = {
		'pronta grossa' : {'country' : 'Brazil',
							'population' : 300000,
							 'fact' : 'coco da uepg'},
							 
		'sao jose do rio preto' : {'country' : 'Brazil',
							'population' : 450000,
							 'fact' : 'great rat'},
							 
		'cornelio procopio' : {'country' : 'Brazil',
								'population' : 50000,
								 'fact' : 'montanhas'}
}



for city,dados in cities.items():
	print("A cidade de " + city.title() + " fica no " +
			dados['country'].title() + ". Com uma população por volta de " + 
			str(dados['population']) + " possui o " + dados['fact'])

#26/07/2021

favorite_languages = {
	'jen' : ['python','ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby','go'],
	'phil' : ['python','haskell'],
	
}

person = ('lucas', 'dalecko', 'phil', 'sarah', 'vinicius')

for people in person:
	if people in favorite_languages.keys():
		print(people.title() + ', obrigado por já ter respodido!!')
	else:
		print(people.title() + ", agradeço se responder a enquete.")

#25/07/2021

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}

#Sempre tentar ser claro no nome das variáveis quando possível
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
			language.title() + ".")
	
print('\nNames:')
	
#O método keys() é conveniente quando não se precisa
	#trabalhar com com tos os valores do dicionários
	#Ele é optativo, use-o caso facilite a leitura do código
for name in favorite_languages.keys():
	print(name.title())

#Utilizando um condicional junto a estrutura de repetição

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	if name in friends:
		print("	Hi, " + name.title() + 
			". I see your favorite language is " +
			favorite_languages[name].title() + "!")

#O método keys() pode ser umado para descobrir se uma chave está no dicionário

if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")		#Faça nossa enquete
	
#É possível usar a função sorted() para obter uma cópia ordenada das chaves
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
	
print('\n')

#Caso haja interesse apenas nos valores é possível usar o método
	#values() da mesma forma como keys()
#Essa abordagem extrai todos os valores sem verificar se há repetição
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
	print(language.title())

print('\n')

#Caso haja a necessidade de se armanezar sem repetição use a função set()
for language in set(favorite_languages.values()):
	print(language.title())

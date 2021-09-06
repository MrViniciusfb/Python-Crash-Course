#31/07/2021
#Lembre-se o método remove() remove apenas o primeiro elemento
pets = ['cat', 'hamister', 'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

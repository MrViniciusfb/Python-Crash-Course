#11/07/2021

#Neste caso, a função começa em 2 e soma 2 até atingir 11
even_numbers = list(range(2,11,2))
print(even_numbers)


#Como fazer o quadrado perfeito dos 10 primeiros números

print("\nMétodo mais longo: ")

squares = []

for value in range(1,11):
	square = value**2
	squares.append(square)

print("\t" + str(squares))

#Porém há um método mais fácil,semre procure o mais fácil

print("\nMétodo mais prático: ")

quadrado_perfeito = []

for value in range(1,11):
	quadrado_perfeito.append(value**2)
	
print("\t" + str(quadrado_perfeito))

#Working with simple statistics
	#There are three typs of functios
		#Function min(), it shows you whats the minimum value of the list
		#Function max(), it shows you whats the maximum value of the list
		#Function sum(),it shows you the list's sum
		
print("\nO menor valor da lista é : " + str(min(quadrado_perfeito)))
print("O maior valor da lista é : " + str(max(quadrado_perfeito)))
print("A soma dos valores da lista é : " + str(sum(quadrado_perfeito)))

#É possível simplificar ainda mais o for visto anteriomente
	#PAra isso é usado a list comprehension
		#Uma list comprehension combina o laço for e a criaçãode novos elementos em uma linha,e concatena cada novo elemento automaticamente
		
print("\nLista feita a partir de uma list comprehension")	
compregension_squares = [value**2 for value in range(1,11)]
print("\t" + str(compregension_squares))

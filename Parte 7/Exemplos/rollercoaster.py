#31/07/2021

#Caso se precise aceitar um input de números, basta usar a função int()

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

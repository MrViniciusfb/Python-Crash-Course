#31/07/2021

#Comparando laço for com laço while
print("--- Contando de 1 a 5 ---")
print("Usando for: ")
for number in range(1, 6):
	print(number)

print("\nUsando while: ")
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
	
print("--- Contando de 1 a 10 pulando um numero ---")
print("Usando for: ")
for number in range(0, 11 , 2):
	print(number)

print("\nUsando while: ")
current_number = -1
while current_number <= 10:
	current_number += 1
	
	if current_number%2 !=0:
		continue
		
	print(current_number)
	

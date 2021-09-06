#19/07/2021

age = 65

#Além do if-else existe também o elif
	#Perceba, o código é executado um atrás do outro, então não há a necessidade
	#de na linha 11 colocar age > 4 and age < 18 como em C,por exemplo

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your adimission cost is $5.")
else:
	print("Your adimission cost is $10.")
	
#Perceba, o código seria melhor estruturado caso fosse escrito assim:

if age < 4:
	preco = 0
elif age < 18:
	preco = 5
elif age < 65:
	preco = 10
#Às vezes é melhor substituir um else por um elif para
	#deixar a compreensão do código mais fácil
elif age >= 65:
	preco = 5
#Percebe-se que o python não exige um else.Isso ocorre porque o else aceita
	#qualquer dado que não cumpra os requisitos dos anterioriores,então pode ser 
	#melhor garantir a precisão do seu código com um elif
print("\nYour adimission cost is $" + str(preco) + ".")

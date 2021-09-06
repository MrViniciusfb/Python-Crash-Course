#11/07/2021

magicians = ['alice','david','carolina']

#Laço são úteis para percorrer um lista e executar nela ações iguais em todos os seus elementos
	#Nunca esquecer de colocar os dois pontos após o for 'SyntaxError: invalid syntax'
	#Para a variável temporária dar nomes sugestivos para ajudar no entendimento
	#O laço percorrerá todos os elementos da lista

for magician in magicians:
	#Caso não se faça nenhuma identação o python irá avisá-lo com o erro 'IdentationError: expected an idented block'
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	#Às vezes também é possível que não ocarra erro,porém o código não funciona da maneira desejada.Verifique, portanto, se os comandos estão dentro do laço identador
		#'Erro de lógica'^ assim como identar algo que deveria vir depois do laço

#Perceba que não estamos mais dentro da identação, logo o código abaixo só será executado uma vez
print("Thank you, everyone. That was a great magic show!")	

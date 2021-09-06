#25/07/2021

glossario = {
			'machine learning' : 'É o aprendizado de máquina',
			'deep learning' : 'Técnica do aprendizado de máquina',
			'data science' : 'Ciência que busca entender os dados',
			'python' : 'Linguagem de programação baseada em interpretador',
			'pandas' : 'Biblioteca do python para data science',
			'logistic regression' : 'É a fórmula para se calcular o erro para um teste',
			'cost function' : 'É a média da regressão logística para todos os testes',
			'sigmoid function' : 'Formato bom para gráficos',
			'Derivada' : 'Taxa de variação'
}

for palavra in glossario:
	print('\n' + palavra + ' : ' + str(glossario[palavra]))

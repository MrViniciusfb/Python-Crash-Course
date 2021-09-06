#26/07/2021

rivers = {
		'nilo' : 'egito',
		'amazonas': 'brazil',
		'amarelo' : 'china'

}

for river in rivers.keys():
	print("O rio " + river.title() + " corre no " + rivers[river].title())

print("\nOs países com importantes rios são:")
for pais in rivers.values():
	print("\t" + pais.title())

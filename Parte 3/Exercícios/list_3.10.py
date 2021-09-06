languages = ['deutsch','português']
print(languages)
print(languages[1].title())
print('Meu idioma materno é o ' + str(languages[1].title()))

languages[1] = 'espanhol'
print(languages)

languages.append('português')
print(languages[-1])
languages.insert(1,'français')
print(languages)

del languages[2]
print(languages)


print(sorted(languages))
print(sorted(languages, reverse = True))
languages.reverse()
print(languages)
languages.reverse()
print(languages)
languages.sort(reverse = True)
print(languages)

popped_languages = languages.pop()
print(languages)
print('Elemento excluido pelo método pop(): ' + str(popped_languages))

dificil = 'français'
languages.remove(dificil)
print(languages)
print(str(dificil.title()) + ' pq é muito dificil')





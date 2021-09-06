#14/07/2021

my_foods = ['pizza','hotdog','tropeiro']
friends_foods = my_foods[:]

my_foods.append('sorvete')
friends_foods.append('bis')
friends_foods.insert(2,'chocolate')

print('My favorite foods are: ')
print('\t' + str(my_foods))

print('\n You always can see it clearly here: ')
for food in my_foods:
	print('\t' + str(food.title()))

print("\nMy friend's favorite foods are:")
print('\t' + str(friends_foods))

print('\n You always can see it clearly here: ')
for food in friends_foods:
	print('\t' + str(food.title()))

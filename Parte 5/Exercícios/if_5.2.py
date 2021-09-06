#18/07/2021

car = 'Subaru'
#TRue
print("Is car == 'subaru' ? I Predict True")
print(car.lower() == 'subaru')

print("\nIs car != 'audi'? I predict True")
print(car.lower() != 'audi')

print("\nIs 'subaru' in car ? I Predict True")
print('subaru' in car.lower())

print("\nIs 'audi' not in car? I predict True")
print('audi' not in car.lower())

print("\nIs car == 'SUBARU' ? I Predict True")
print(car.upper() == 'SUBARU')


#False
print("\nIs car == 'audi'? I predict False")
print(car.lower() != 'subaru')

print("\nIs 'audi' in car? I predict False")
print('audi' in car.lower())

print("\nIs 'subaru' not in car? I predict False")
print('subaru' not in car.lower())

print("\nIs car == 'audi'? I predict False")
print(car.lower() == 'audi')

#Numerico
age_0 = 18
age_1 = 20

print("\nIs age_0 > 18 and age_1 > 18? I predict False")
print(age_0 > 18 and age_1 > 18)

print("\nIs age_0 >= 18 and age_1 >= 20? I predict True")
print(age_0 >= 18 and age_1 >= 20)

print("\nIs age_0 > 18 or age_1 > 18? I predict True")
print(age_0 > 18 or age_1 > 18)

#Lista
pizzas = ['peperoni','mussarela','fish']

print("\nIs peperoni in pizzas? I predict True")
print('peperoni '.strip() in pizzas)

print("\nIs mushroom in pizzas? I predict True")
print('mushroom ' in pizzas)

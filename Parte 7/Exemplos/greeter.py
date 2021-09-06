#31/07/2021

#Para aceitar entradas de usuários é necessário usar a função input()

#E caso seu prompt seja muito grande, basta fazer a seguir:

prompt = "If you tell us who you are, wecan personalize the messages you see."
prompt += "\nWhat is you first name? " #+= junta strings

name = input(prompt)
print("\nHello, " + name + "!")

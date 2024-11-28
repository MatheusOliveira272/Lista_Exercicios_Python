'''
11. Crie um algoritmo que leia um número inteiro. Se o número lido for positivo, escreva uma mensagem 
indicando se ele é par ou ímpar. 
'''

# Solicitar um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é positivo
if numero > 0:
    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("O número não é positivo.")

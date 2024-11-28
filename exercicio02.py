'''
2.	Crie um algoritmo que receba um número do usuário e mostre o número e o seu dobro somente quando o número for maior que noventa e menor que cem.
'''

# Solicitar um número do usuário
numero = float(input("Digite um número: "))

# Verificar se o número está entre 90 e 100
if 90 < numero < 100:
    dobro = numero * 2
    print(f"O número é {numero} e o seu dobro é {dobro}.")
else:
    print("O número não está entre 90 e 100.")

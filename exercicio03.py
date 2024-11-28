'''
3.	Construa um algoritmo que receba um número do usuário e mostre o seu sêxtuplo somente quando o resultado não for menor que trezentos.
'''

# Solicitar um número do usuário
numero = float(input("Digite um número: "))

# Calcular o sêxtuplo do número
sextuplo = numero * 6

if sextuplo >= 300:
    print(f"O sêxtuplo de {numero} é {sextuplo}.")
else:
    print("O sêxtuplo é menor que 300.")
